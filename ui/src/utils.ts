export const getDate = () => { return new Date(Date.now()) }

export function getISODateString(date: Date) {
    return date.toISOString().split('T', 1)[0]
}

export function getDateString(date: Date) {
    let month_string = (date.getMonth() + 1).toString()
    if (month_string.length === 1)
        month_string = '0' + month_string
    return date.getFullYear() + '-' + month_string + '-' + date.getDate()
}

export function getDateFromISOString(date: string) {
    const finalDate = new Date()
    const splitString = date.split('-')
    finalDate.setFullYear(parseInt(splitString[0]))
    finalDate.setMonth(parseInt(splitString[1]) - 1)
    finalDate.setDate(parseInt(splitString[2]))

    return finalDate
}