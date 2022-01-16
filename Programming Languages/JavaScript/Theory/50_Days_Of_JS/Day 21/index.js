const unionOfArrays = (arr1, arr2) => {
  // code below here
  const arraySet2 = new Set(arr1)
    let finalArray = [...arr1]

    for(let element of arr2){
        if(!arraySet2.has(element)){
            finalArray.push(element)
        }
    }

    return finalArray;
};

console.log(`The union is ${unionOfArrays([1, 2, 34, 45, 3], [3, 24, 21])}`);
