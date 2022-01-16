var NUMBER2TEXT = {
  ones: [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
  ],
  tens: [
    "",
    "",
    "twenty",
    "thirty",
    "fourty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
  ],
  sep: [
    "",
    " thousand ",
    " million ",
    " billion ",
    " trillion ",
    " quadrillion ",
    " quintillion ",
    " sextillion ",
  ],
};

const { ones, tens, sep } = NUMBER2TEXT;

const sayNumberInEnglish = (number) => {
  let arr = [],
    str = "",
    i = 0;
  if (number.length === 0) {
    return;
  }

  number = parseInt(number, 10);
  if (isNaN(number)) {
    return;
  }

  while (number) {
    arr.push(number % 1000);
    number = parseInt(number / 1000, 10);
  }

  while (arr.length) {
    str =
      (function (a) {
        var x = Math.floor(a / 100),
          y = Math.floor(a / 10) % 10,
          z = a % 10;

        return (
          (x > 0 ? ones[x] + " hundred " : "") +
          (y >= 2 ? tens[y] + "-" + ones[z] : ones[10 * y + z])
        );
      })(arr.shift()) +
      sep[i++] +
      str;
  }

  return str;
};

console.log(`5635 in english is: ${sayNumberInEnglish(5635)}`);
