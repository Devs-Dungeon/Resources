const obj = { key: 1 };

function isEmpty(obj) {
    // write your solution here

    return Object.entries(obj).length === 0
}

console.log(`is empty object: ${isEmpty(obj)}`)
