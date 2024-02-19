import { get } from 'svelte/store';
import { APIToken, APITokenExpiry } from '@stores/auth';
import { fatalNavigationError } from '@stores/error';
import { APIUrl } from './base';

export class NetworkError {
	status: number;
	message: string;
	response: Response;
	constructor(status: number, message: string, response: Response) {
		this.status = status;
		this.message = message;
		this.response = response;
	}
}

export async function authenticatedAPICall(
	method: 'POST' | 'GET' | 'DELETE' | 'PATCH',
	endpoint: string,
	body: Object = {},
	parseJSON: boolean = false,
	failOnError: boolean = false
) {
	return fetch(`${APIUrl}/api/${endpoint}`, {
		method: method,
		mode: 'cors',
		body: ['POST', 'PATCH'].includes(method) ? JSON.stringify(body) : undefined,
		headers: {
			Authorization: `Token ${get(APIToken)}`,
			'Content-Type': 'application/json'
		}
	}).then((response) => {
		if (response.ok)
			if (parseJSON) return response.json();
			else return response;

		if (failOnError && (response.status === 404 || response.status === 403))
			fatalNavigationError.set(true);

		throw new NetworkError(response.status, response.statusText, response);
	});
}
