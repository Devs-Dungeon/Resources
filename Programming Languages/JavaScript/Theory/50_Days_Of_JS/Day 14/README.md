# Convert given array of digits of a base to another asked base

## Instructions

- Convert a number, represented as a sequence of digits in one base, to any other base.
- Implement general base conversion. Given a number in base a, represented as a sequence of digits, convert it to base b.

## Example

- input: convertDigitsToAskedBase([5, 8], 10, 16)
- output: [3, 10]

**convertDigitsToAskedBase([5, 8], 10, 16) is passed to the convertDigitsToAskedBase function i.e 58 in base 10 as [5, 8] in array is passed and asked to convert to base 16 which is 310. This should be returned in array as [3, 10].**

## Note
- [3, 10] is not other than [3, 10] is because 3 and 10 both are valid digits of base 16
- [3, 1, 0] is WRONG because even though 1 and 0 are valid digits of base 16 it can be represented as 10 without taking the 3rd place.

## Challenges (0/2 done)
- [ ] convertDigitsToAskedBase([5, 8], 10, 16) should return [3, 10]
- [ ] convertDigitsToAskedBase() with any random value passed should return correct array as asked

```js
/**
 *
 * @param {number[]} digits Array of valid digits of baseA
 * @param {number} baseA base a
 * @param {number} baseB base b in which digits are to be converted
 * @returns {number[]} Array of valid digits of baseB
 */
const convertDigitsToAskedBase = (digits, baseA, baseB) => {
	// Your code here

	return
}
```
