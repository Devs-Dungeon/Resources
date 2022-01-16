function isIsogram(str) {
  // your code here
  return new Set(str.toLowerCase()).size === str.length;
}
