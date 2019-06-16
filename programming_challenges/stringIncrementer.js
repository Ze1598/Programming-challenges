// https://www.codewars.com/kata/string-incrementer/python
/*
Write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number, the number 1 should be appended to the
new string.
If the number has leading zeros, the amount of digits should be considered.

Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
*/

// Check if a string contains digits
function containsDigits (string) {
	return /\d/.test(string);
}

// Main function to increment the trailing number in a given string
function stringIncremeter (string) {
	// Empty string
	if (string === "") {
		return "1";
	}
	
	// String contains only letters, thus just prefix it with a one
	else if (containsDigits(string) === false) {
		return string + "1";
	}
	
	// The string does not contain only letters, but its last character\
	// is not a digit (thus it counts as if it contained only letters)
	else if (containsDigits(string[string.length-1]) === false) {
		return string + "1";
	}
	
	// The string does not contain only letters and its last character\
	// is a number (confirms that at least one digit is at the end\
	// of the string and not somewhere else)
	else if (containsDigits(string[string.length-1]) === true) {
		// We are looking for as many (one or more) digits the string has at\
		// the end
		var regEx = new RegExp(/[0-9]+$/);
		// Search for the regular expression and obtain the extracted number\
		// (as a string)
		// `exec()` returns an array containing: [matchedText, matchStartIndex\
		// (index), testedString (input), groups]
		var stringMatch = regEx.exec(string);
		// Index of the first character matched (used to remove the original\
		// number when creating the incremented string)
		var matchStart = stringMatch.index;

		// If the number doesn't have trailing zeroes, simply increment it\
		// by one and suffix it to the string (removing the original number\
		// from the string)
		// (is the length of the number found in the string equal to the length\
		// of the incremented number?)
		if (stringMatch[0].length === parseInt(stringMatch[0]).toString().length) {
			return string.slice(0, matchStart) + (parseInt(stringMatch[0])+1).toString();
		}

		// The number has trailing zeroes
		else {
			// Increment the extracted number
			var incNum = parseInt(stringMatch[0]) + 1;
			// If, after being incremented, the number has the same length as the\
			// original number with trailing zeroes, suffix it to the string with no\
			// further changes (without the original number) (e.g., "099" -> 99 -> 100)
			if (incNum.toString().length === stringMatch[0].length){
				return string.slice(0, matchStart) + incNum.toString();
			}

			// If the incremented number is missing trailing zeroes, add the necessary\
			// zeroes and then add the number to the string
			else {
				// Add as many trailing zeroes as necessary until the incremented number\
				// has as many digits as the extracted number from the input string
				var numToAdd = incNum.toString().padStart(stringMatch[0].length, 0);
				// Finally, create the incremented string
				return string.slice(0, matchStart) + numToAdd;
			}
		}
	}
}


var strings = ["foo", "foobar001", "foobar1", "foobar00", "foo099", ""]
console.log("Increment strings:\n")
for (s of strings) {
	console.log(`${s} => ${stringIncremeter(s)}\n`)
}