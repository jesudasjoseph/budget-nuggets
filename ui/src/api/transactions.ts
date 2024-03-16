import { authenticatedAPICall } from './util';
import { getDateFromISOString } from '@/utils';

export async function listTransactions(budget: number, period: number | undefined = undefined, from_date: Date | undefined = undefined, to_date: Date | undefined = undefined) {
    let params = `?budget=${budget}`

    if (period)
        params += `&period=${period}`

    if (from_date)
        params += `&from_date=${from_date}`

    if (to_date)
        params += `&to_date=${to_date}`

    return authenticatedAPICall(
        'GET',
        `transactions/${params}`,
        undefined,
        true
    )
}

interface PeriodCategory {
    "value": number;
    "period_category": number;
}

export async function createTransaction(budget: number, period: number, value: number, merchant: string | undefined, notes: string | undefined, date: Date, periodCategories: PeriodCategory[] = []) {
    return authenticatedAPICall(
        'POST',
        'transactions/',
        {
            budget,
            period,
            value,
            merchant,
            notes,
            date,
            "period_categories": periodCategories
        },
        true
    )
}