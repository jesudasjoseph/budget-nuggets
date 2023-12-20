import { writable, derived } from 'svelte/store';

function createAPIToken() {
	const startValue = localStorage.getItem('token');
	const { subscribe, set, update } = writable(startValue);

	function setValue(value: string) {
		localStorage.setItem('token', value);
		set(value);
	}

	return {
		subscribe,
		set: (n: string) => setValue(n)
	};
}

export const APIToken = createAPIToken();

function createAPITokenExpiry() {
	const startValue = localStorage.getItem('token-expiry');
	const { subscribe, set, update } = writable(startValue);

	function setValue(value: string) {
		localStorage.setItem('token-expiry', value);
		set(value);
	}

	return {
		subscribe,
		set: (n: string) => setValue(n)
	};
}

export const APITokenExpiry = createAPITokenExpiry();

export const isLoggedIn = derived([APIToken, APITokenExpiry], ([$APIToken, $APITokenExpiry]) => {
	if ($APITokenExpiry && $APIToken) {
		return new Date($APITokenExpiry) > new Date();
	}
});
