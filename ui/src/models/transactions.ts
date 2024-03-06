export interface Transaction {
    id: number
    value: string
    merchant: string
    notes?: string
    date: string
    budget: number
    period: number
    user: number
    period_categories: number[]
}