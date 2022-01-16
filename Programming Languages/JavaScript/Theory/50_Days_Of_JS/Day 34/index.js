function mostFreq(arr) {
	// write your code here
    if (arr.length === 0) return -1

    if (arr.length === 1) return [arr[0], 1]

    const numMap = new Map()

    for(let num of arr){
        let currentNum = numMap.get(num)

        if(currentNum === undefined) numMap.set(num, 1)
        else numMap.set(num, currentNum + 1)
    }

    const numArray = [undefined, undefined]

    for(let [key, value] of numMap){
        if(numArray[1] === undefined || numArray[1] < value) {
            numArray[0] = key
            numArray[1] = value
        }
    }

    return numArray[0].toString()+' '+numArray[1].toString()
}

const arr = [1, 2, 2, 4, 5, 6, 6];

console.log(mostFreq(arr));
