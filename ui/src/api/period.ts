import { authenticatedAPICall } from './util';

export async function createPeriod(date: Date, budget_id: number) {
	return authenticatedAPICall(
		'POST',
		`period/create/`,
		{
			date: date.toISOString().split('T', 1)[0],
			budget: budget_id
		},
		true
	);
}

export async function getPeriodByID(period_id: number) {
	return authenticatedAPICall('GET', `period/${period_id}/`, true);
}

export async function getPeriodByDate(date: Date, budget_id: number) {
	return authenticatedAPICall(
		'GET',
		`period/?budget=${budget_id}&date=${date.toISOString().split('T', 1)[0]}`,
		undefined,
		true
	);
}
