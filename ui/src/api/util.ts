import { get } from "svelte/store";
import { APIToken, APITokenExpiry } from "../stores";

export async function authenticatedAPICall(method: 'POST' | 'GET', endpoint: string, body: Object = {}) {
    const response = await fetch(`http://127.0.0.1:8000/${endpoint}`, {
        method: method,
        mode: 'cors',
        body: JSON.stringify(body),
        headers: {
            Authorization: `Token ${get(APIToken)}`,
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        if (!response.ok) {
            throw new Error(`Network Error: ${response.status} - ${response.statusText}`);
        }
        if (response.status !== 204)
            return response.json();
    }).catch((error) => {
        console.error(error);
    });
}

export async function loginAPICall(username: string, password: string) {
    const response = await fetch(`http://127.0.0.1:8000/auth/login/`, {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify({ username: username, password: password }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((response) => {
        if (!response.ok) {
            throw new Error(`Network Error: ${response.status} - ${response.statusText}`);
        }
        return response.json();
    }).then((data) => {
        APIToken.set(data.token);
        APITokenExpiry.set(data.expiry);
    });;
}