function sumTwoSmallestNumbers(numbers) {
  //Code below
  numbers.sort((a,b)=>(a-b));
  return (numbers[0]+numbers[1]);
}
