// Find and sum the two smallest integers in a given array
// Find and sum the two largest integers in a given array

// Find and sum the two smallest integers in a given array
function sumTwoSmallestNumbers(numbers) {
	// Declare the variables to hold the two smallest numbers in the array
	// The smallest number in the array
	let smallest = numbers[0];
	// The second-smallest number in the array
	let small2 = numbers[0];

	// Loop through the array
	for (let i=0; i<numbers.length; i++) {

		// If the number is bigger than the smallest number
		if (smallest < numbers[i]){

			// If the number is bigger than the smallest and smaller than\
			// the 2nd-smallest OR the number is bigger than the smallest\
			// and the two smallest numbers are equal, THEN the 2nd-smallest\
			// is now the current number
			// If (smallest < num < small2) OR\
			// (num > smallest == small2)
			if ( (small2 > numbers[i]) || (smallest == small2) ) {
				small2 = numbers[i];
			}
		}

		// If the number is equal to or smaller than the smallest number
		else {

			// If the 2nd-smallest is bigger than the smallest AND the number\
			// is different from the smallest, THEN what was the smallest now\
			// becomes the 2nd-smallest
			// If (num < smallest < small2) AND\
			// (num != smallest < small2)
			if ( (smallest < small2) && (smallest != numbers[i]) ) {
				small2 = smallest;
			}

			// If the number is equal to or smaller than the smallest number,\
			// THEN the current number will always be assigned as the new\
			// smallest number
			smallest = numbers[i];
		}
	}

	// Return the sum of the two smallest numbers
	return smallest + small2;
}

// Find and sum the two largest integers in a given array
function sumTwoLargestNumbers(numbers) {
	// Declare the variables to hold the two largest numbers in the array
	// The largest number in the array
	let largest = numbers[0];
	// The second-largest number in the array
	let large2 = numbers[0];

	// Loop through the array
	for (let i=0; i<numbers.length; i++) {

		// If the number is smaller than the largest number
		if (largest > numbers[i]) {

			// If the number is smaller than the largest and bigger than\
			// the 2nd-largest OR the number is smaller than the largest\
			// and the two largest numbers are equal, THEN the 2nd-largest\
			// is now the current number
			// If (largest > numbers[i] > large2) OR\
			// (numbers[i] > largest == large2)
			if ( (large2 < numbers[i])  || (largest == large2) ) {
				large2 = numbers[i];
			}
		}

		// If the number is equal to or larger than the largest number
		else {

			// If the 2nd-largest is smaller than the largest AND the number\
			// is different from the largest, THEN what was the largest now\
			// becomes the 2nd-largest
			// IF (num > largest > large2) AND\
			// (num != largest > large2)
			if ( (largest > large2) && (largest != numbers[i]) ) {
				large2 = largest;
			}

			// If the number is equal to or larger than the largest number,\
			// THEN the current number will always be assigned as the new\
			// largest number
			largest = numbers[i];
		}
	}

	// Return the sum of the two largest numbers
	return largest + large2;
}

function main() {
	// Create a sample array
	var sample = [97, 53, 21, 19, 19];
	// Output the sum of the two smallest integers in the array
	console.log("sumTwoSmallestNumbers([97, 53, 21, 19, 19]) =>", sumTwoSmallestNumbers(sample));
	// Output the sum of the two largest integers in the array
	console.log("sumTwoLargestNumbers([97, 53, 21, 19, 19]) =>", sumTwoLargestNumbers(sample));
}

main()