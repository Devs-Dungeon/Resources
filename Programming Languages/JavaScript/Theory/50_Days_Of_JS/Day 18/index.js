const totalGrains = () => {
    // Code here
    let ans = BigInt(0);
    for(let i =0;i<64;i++)
    {
        ans += BigInt(2**i);
    }
	return ans;
}

const grainsOn = (input) => {
	// Code here
	return BigInt(2**(input-1));
}

console.log(`Grains on 5th square: ${grainsOn(5)}`)
console.log(`Total grains upto 5th square: ${totalGrains()}`)
