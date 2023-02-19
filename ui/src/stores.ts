import { writable } from 'svelte/store';

export const APIToken = writable(null);
export const APITokenExpiry = writable(null);
export const isAuthenticated = writable(false);