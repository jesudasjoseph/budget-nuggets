import type { Category } from "./categories"

export interface Period {
    id: number
    start_date: Date
    end_date: Date
    label: string
    budget: number
}

export interface PeriodCategory {
    id: number
    value: string
    budget: number
    category: Category
}