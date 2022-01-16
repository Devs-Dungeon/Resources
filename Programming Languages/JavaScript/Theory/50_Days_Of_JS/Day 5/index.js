const str = 'XeroX';

function getTheGapX(str) {
    // write your solution here
    const firstIndex = str.indexOf('X')

    if(firstIndex === -1){
        return -1
    }

    const lastIndex = str.lastIndexOf('X')

    if(firstIndex === lastIndex){
        return 0
    }

    return lastIndex - firstIndex
}

console.log(`Gap between the X's: ${getTheGapX(str)}`)
