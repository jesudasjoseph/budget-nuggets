import { authenticatedAPICall } from './util';

export async function listTransactions(budget: number, period: number | undefined = undefined, from_date: Date | undefined = undefined, to_date: Date | undefined = undefined, period_category: number | undefined = undefined) {
    let params = `?budget=${budget}`

    if (period)
        params += `&period=${period}`

    if (from_date)
        params += `&from_date=${from_date}`

    if (to_date)
        params += `&to_date=${to_date}`

    if (period_category)
        params += `&period_category=${period_category}`

    return authenticatedAPICall(
        'GET',
        `transactions/${params}`,
        undefined,
        true
    )
}

interface PeriodCategory {
    "value": string;
    "period_category": string;
}

export async function createTransaction(budget: number, period: number, value: string, merchant: string | undefined, notes: string | undefined, date: Date | string, periodCategories: PeriodCategory[] = []) {
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