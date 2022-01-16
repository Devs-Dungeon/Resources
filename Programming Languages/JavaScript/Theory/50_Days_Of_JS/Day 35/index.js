function nthlargest(arr, highest) {
	// write your code here
    arr.sort((a, b)=>(a-b));
    console.log(arr);
	return arr[(arr.length-highest)];
}

const arr = [43, 56, 23, 89, 88, 90, 99, 652];
const highest = 4;

console.log(nthlargest(arr, highest));
