import { authenticatedAPICall } from './util';

export async function createCategoryAPI(budget: number, label: string) {
    return authenticatedAPICall('POST', 'categories/', { budget, label }, true);
}

export async function listCategories(budget: number) {
    return authenticatedAPICall('GET', `categories/?budget=${budget}`, undefined, true);
}

export async function updateCategory(category_id: number, label: string | undefined = undefined, color: string | undefined = undefined) {
    return authenticatedAPICall('PATCH', `categories/${category_id}/`, { label, color }, true);
}