export const getDate = () => { return new Date(Date.now()) }

export function getDateFromISOString(date: string) {
    const finalDate = new Date()
    const splitString = date.split('-')
    finalDate.setFullYear(parseInt(splitString[0]))
    finalDate.setMonth(parseInt(splitString[1]) - 1)
    finalDate.setDate(parseInt(splitString[2]))

    return finalDate
}