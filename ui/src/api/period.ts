import { authenticatedAPICall } from './util';
import { getDateFromISOString } from '@/utils';

export async function createPeriod(date: Date, budget_id: number) {
	return authenticatedAPICall(
		'POST',
		'periods/',
		{
			date: date.toISOString().split('T', 1)[0],
			budget: budget_id
		},
		true
	);
}

export async function createNextPeriodAPI(period_id: number, budget_id: number) {
	return authenticatedAPICall(
		'POST',
		'periods/create_next/',
		{
			period: period_id,
			budget: budget_id
		},
		true
	)
}

export async function getPeriodByID(period_id: number) {
	return authenticatedAPICall('GET', `periods/${period_id}/`, undefined, true);
}

export async function listPeriods(budget_id: number) {
	return authenticatedAPICall('GET', `periods/?budget=${budget_id}`, undefined, true).then((response) => {
		return response.map((period: any) => {
			period.start_date = getDateFromISOString(period.start_date);
			period.end_date = getDateFromISOString(period.end_date);
			return period
		})
	})
}


export async function getPeriodByDate(date: Date, budget_id: number) {
	return authenticatedAPICall(
		'GET',
		`periods/?budget=${budget_id}&date=${date.toISOString().split('T', 1)[0]}`,
		undefined,
		true
	);
}

export async function getPeriodCategoryAPI(period_id: number, period_category_id: number) {
	return authenticatedAPICall('GET', `periods/${period_id}/categories/${period_category_id}/`, undefined, true)
}

export async function listPeriodCategoriesAPI(period_id: number) {
	return authenticatedAPICall('GET', `periods/${period_id}/categories/`, undefined, true);
}

export async function createPeriodCategoryAPI(period_id: number, category_id: number, value: string) {
	return authenticatedAPICall('POST', `periods/${period_id}/categories/`, { period: period_id, category: category_id, value }, true)
}

export async function deletePeriodCategoryAPI(period_id: number, period_category_id: number) {
	return authenticatedAPICall('DELETE', `periods/${period_id}/categories/${period_category_id}/`);
}