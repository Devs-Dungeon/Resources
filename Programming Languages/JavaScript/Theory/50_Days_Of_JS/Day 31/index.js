function factorial(n) {
	// write your code here
    if(n===0 || n===1)
        return 1;
	return factorial(n-1) * n;
}

let n = 4;
console.log("The factorial of " + n + " is " + factorial(n));
