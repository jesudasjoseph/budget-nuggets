import { get } from 'svelte/store';
import { APIToken, APITokenExpiry } from '@stores/auth';
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
	method: 'POST' | 'GET',
	endpoint: string,
	body: Object = {},
	parseJSON: boolean = false
) {
	return fetch(`${APIUrl}/api/${endpoint}`, {
		method: method,
		mode: 'cors',
		body: method === 'POST' ? JSON.stringify(body) : undefined,
		headers: {
			Authorization: `Token ${get(APIToken)}`,
			'Content-Type': 'application/json'
		}
	})
		.then((response) => {
			if (!response.ok) throw new NetworkError(response.status, response.statusText, response);
			return response;
		})
		.then((response) => {
			if (parseJSON) {
				return response.json();
			}
		});
}

export async function loginAPICall(username: string, password: string) {
	const response = await fetch(`http://127.0.0.1:8000/api/auth/login/`, {
		method: 'POST',
		mode: 'cors',
		body: JSON.stringify({ username: username, password: password }),
		headers: {
			'Content-Type': 'application/json'
		}
	})
		.then((response) => {
			if (!response.ok) {
				throw new NetworkError(response.status, response.statusText, response);
			}
			return response.json();
		})
		.then((data) => {
			APIToken.set(data.token);
			APITokenExpiry.set(data.expiry);
		});
}

export async function getUserAccounts() {
	return authenticatedAPICall('POST', '/accounts');
}
