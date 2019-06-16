// https://leetcode.com/problems/two-sum/
/*
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input will have exactly one solution, and you may
not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

// Loop only once through the input array and, as we loop, save the checked\
// values in a HashMap of pairs value-valueIndex, so that every iteration\
// we can check if the current number's complement has already been found:\
// if it has, return an array with the two indices, otherwise add the\
// current number to the map and move to the next iteration
function twoSum (nums, target) {
	// Object to map checked values to their indices
	var previousValues = {}

	// Now loop through the array
	for (let i=0; i<nums.length; i++) {
		// Number we are looking at from the array
		var currentNumber = nums[i];
		// Calculate the complement needed
		var neededNumber = target - currentNumber;
		// Index of the complement number (if the number is not present\
		// in the map, then this variable will be `null`)
		var neededIndex = previousValues[neededNumber]
		// If the complement number has already been found, then return\
		// the two target indices
		if (neededIndex != null) {
			return [neededIndex, i];
		}
		// Otherwise, add the current number to the map and move on to the\
		// next iteration
		previousValues[currentNumber] = i;
	}
}

console.log( twoSum([2, 7, 11, 15], 9) )