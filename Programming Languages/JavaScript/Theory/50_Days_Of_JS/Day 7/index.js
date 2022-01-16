const number = '+919876543210';

function validateMobile(number) {
    // write your solution here
    const numberMatchingRegex = /^(\+91|0)?\s?\d{10}$/

    const result = numberMatchingRegex.test(number)

    return result
}

console.log(`is a valid Indian mobile number: ${validateMobile(number)}`)
