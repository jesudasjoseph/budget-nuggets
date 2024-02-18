import { authenticatedAPICall } from './util';

export async function createBudget(name: string, type: 'AN' | 'MN' | 'BW' | 'W' | 'EV') {
	return authenticatedAPICall('POST', 'budgets/', { name, type }, true);
}

export async function listBudgets() {
	return authenticatedAPICall('GET', 'budgets/', undefined, true);
}

export async function getBudget(id: number) {
	return authenticatedAPICall('GET', `budgets/${id}/`, undefined, true, true);
}

export async function deleteBudget(id: number) {
	return authenticatedAPICall('DELETE', `budgets/${id}/`);
}
