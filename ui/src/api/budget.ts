import { authenticatedAPICall } from './util';

export async function createBudget(name: string, type: 'AN' | 'MN' | 'BW' | 'W' | 'EV') {
	return authenticatedAPICall('POST', 'budget/create/', { name, type }, true);
}

export async function listBudgets() {
	return authenticatedAPICall('GET', 'budget/', undefined, true);
}

export async function getBudget(id: number) {
	return authenticatedAPICall('GET', `budget/${id}/`, undefined, true, true);
}