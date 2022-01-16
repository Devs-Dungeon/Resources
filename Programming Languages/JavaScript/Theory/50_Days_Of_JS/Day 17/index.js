/**
 *
 * @param {number[]} inputArray Array of numbers
 */
const longestConsecutiveSequence = (inputArray) => {
    // Your code here
    if(!inputArray.length) return 0

    const set = new Set(inputArray)
    let max = 0

    for(const num of set){
        if(set.has(num-1)) continue

        let currNum = num
        let currMax = 1

        while (set.has(currNum + 1)){
            currNum++
            currMax++
        }

        max = Math.max(max, currMax)
    }

    return max
}
