function expandedForm(num) {
  // Your code here
  const currentNumArray = num.toString().split('')
    let currentMultiplyingFactor = 1
    let currentPos = currentNumArray.length - 1

    while(currentPos >= 0){
        currentNumArray[currentPos] = (parseInt(currentNumArray[currentPos]) * currentMultiplyingFactor).toString()
        currentMultiplyingFactor *= 10
        currentPos--
    }

    return (currentNumArray.join('+')).trim()
}
