import PeriodCategory from "@components/PeriodCategory.svelte"

export interface Transaction {
    id: number
    value: string
    merchant: string
    notes?: string
    date: string
    budget: number
    period: number
    user: number
    period_categories: PeriodCategory[]
}