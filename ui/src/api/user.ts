import { APIUrl } from './base';
import { NetworkError } from './util';

export async function createUser(
	email: string,
	firstName: string,
	lastName: string,
	password: string,
	passwordConfirmation: string
) {
	return fetch(`${APIUrl}/api/user/create/`, {
		method: 'POST',
		mode: 'cors',
		body: JSON.stringify({
			email: email,
			first_name: firstName,
			last_name: lastName,
			password: password,
			password_confirmation: passwordConfirmation
		}),
		headers: {
			'Content-Type': 'application/json'
		}
	}).then((response) => {
		if (!response.ok) {
			throw new NetworkError(response.status, response.statusText, response);
		}
		return response.json();
	});
}
