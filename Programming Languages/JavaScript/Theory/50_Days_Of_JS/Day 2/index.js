const str = "JavaScript is awesome"

function reverseAString(str) {
    // write your solution here
    var newString = "";
    for (var i = str.length - 1; i >= 0; i--) {
        newString += str[i];
    }

    return newString
}

console.log(`Reversed string is: ${reverseAString(str)}`)
