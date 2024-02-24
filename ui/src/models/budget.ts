export type Types = 'AN' | 'MN' | 'BW' | 'W' | 'EV';

export interface Budget {
    id: number
    name: string
    type: Types
    owner: number
    users: number[]
}