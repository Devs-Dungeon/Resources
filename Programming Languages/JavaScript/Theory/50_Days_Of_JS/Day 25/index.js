function spinWords(string) {
  string = string.split(" ");
  string = string.map((str) => {
    return str.length > 4 ? str.split("").reverse().join("") : str;
  });
  return string.join(" ");
}
