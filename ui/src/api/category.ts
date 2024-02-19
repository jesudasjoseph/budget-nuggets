import { authenticatedAPICall } from './util';

export async function listCategories(budget: number) {
    return authenticatedAPICall('GET', `categories/?budget=${budget}`, undefined, true);
}