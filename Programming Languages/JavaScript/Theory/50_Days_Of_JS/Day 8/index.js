const DAY_IN_MILLISECONDS = 1000 * 60 * 60 * 24;

function getDaysBetweenDates(dateText1, dateText2) {
    // write your solution here

    const day1 = new Date(dateText1)
    const day2 = new Date(dateText2)
    const DifferenceInTime = Math.abs(day2.getTime() - day1.getTime())
    return DifferenceInTime / DAY_IN_MILLISECONDS
}

console.log(`Days difference: ${getDaysBetweenDates('10/15/2020', '12/1/2020')}`)
