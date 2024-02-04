import { authenticatedAPICall } from './util';

export async function createPeriod(date: Date, budget_id: number) {
	return authenticatedAPICall(
		'POST',
		`budget/${budget_id}/period/create/`,
		{
			date: date.toISOString().split('T', 1)[0]
		},
		true
	);
}

export async function getPeriodByID(period_id: number, budget_id: number) {
	return authenticatedAPICall('GET', `budget/${budget_id}/period/${period_id}/`, true);
}

export async function getPeriodByDate(date: Date, budget_id: number) {
	return authenticatedAPICall(
		'GET',
		`budget/${budget_id}/period?date=${date.toISOString().split('T', 1)[0]}`,
		undefined,
		true
	);
}
