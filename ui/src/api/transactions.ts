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