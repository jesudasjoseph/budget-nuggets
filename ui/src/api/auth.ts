import { NetworkError, authenticatedAPICall } from './util';
import { APIToken, APITokenExpiry } from '@stores/auth';

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

export async function logoutallAPICall() {
	return authenticatedAPICall('POST', 'auth/logoutall/');
}
