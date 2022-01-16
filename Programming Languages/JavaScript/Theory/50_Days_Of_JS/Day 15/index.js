const isPangram = (input) => {
    // Code here
    const ALPHABET_ARRAY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    const inputArray = input.toLowerCase().split('')
    let isItAPangram = true

    ALPHABET_ARRAY.forEach(alphabet => {
        if(!inputArray.includes(alphabet)){
            isItAPangram = false
        }
    })

    return isItAPangram
}

console.log(isPangram('The quick brown fox jumps over the lazy dog.'))
