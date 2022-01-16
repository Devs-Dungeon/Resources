let uniqueInOrder = (iterable) => {
  //your code here - remember iterable can be a string or an array
  let arr = [];
  for (var i = 0; i < iterable.length; i++) {
    if (iterable[i] !== iterable[i + 1]) arr.push(iterable[i]);
  }
  return arr;
};
