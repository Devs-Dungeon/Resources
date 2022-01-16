function getDivisorsCnt(num) {
  // code below
  if(num === 1) return 1
    if(num === 2 || num === 3) return 2

    let totalNumOfDivisors = 2
    let startingPoint = 2
    let endingPoint = Math.ceil(num / 2)

    while (startingPoint <= endingPoint){
        if(num % startingPoint === 0) totalNumOfDivisors++

        if(startingPoint === endingPoint){
            startingPoint++
            endingPoint--
            continue
        }

        if(num % endingPoint === 0) totalNumOfDivisors++

        startingPoint++
        endingPoint--
    }

    return totalNumOfDivisors
}
