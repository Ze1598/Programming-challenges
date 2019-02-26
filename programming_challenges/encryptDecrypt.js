// https://www.codewars.com/kata/57814d79a56c88e3e0000786/solutions/cpp
/*
Take every second character from an input string, then concatenate the
remaining characters to that to create an encrypted string. This operation
is done n times.
Examples:
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two functions:
encrypt(text, n)
decrypt(encryptedText, n)
Extra rules:
If the input string is empty then return an empty string.
If n is <= 0 then return the input string.
*/

function encrypt (text, n) {
	if (text === "") {
		return "";
	}
	else if (n < 0) {
		return text;
	}
	else {
		// The temporary string starts as the input string
		let temp_string = text;
		// This contains all the second characters from the input string
		let first_half = "";
		// This contains all the first characters from the input string
		let second_half = "";

		// Encrypt the input string `n` times
		for (let encryption=0; encryption<n; encryption++) {


			// Loop through the string to save every second character to\
			// `first_half`
			for (let i=1; i<temp_string.length; i+=2) {
				first_half += temp_string[i];
			}

			// Loop through the string to save every second character to\
			// `second_half`
			for (let i=0; i<temp_string.length; i+=2) {
				second_half += temp_string[i];
			}

			// Update `temp_string` to concatenate both halves
			temp_string = first_half + second_half;
			// Reset both halves to empty strings
			first_half = "";
			second_half = "";
		}

		// Finally, return the encrypted string
		return temp_string
	}
}

function decrypt (encryptedText, n) {
	if (encryptedText === "") {
		return "";
	}
	else if (n < 0) {
		return encryptedText;
	}
	else {
		
		// The temporary string starts as the input string
		let temp_string = encryptedText;
		// Variable to hold the result of each decryption
		let result = "";

		for (let decryption=0; decryption<n; decryption++) {
			// Middle index of `temp_string`
			let half = parseInt(temp_string.length / 2);

			// When the middle index is odd
			if (temp_string.length%2 != 0) {
				// Loop through the `temp_string` string, starting at the middle\
				// and, each iteration, add to the `result` the character at the\
				// current index and the one `half` indices behind
				for (let i=half; i<temp_string.length; i++) {
					result += temp_string[i];
					result += temp_string[i-half];
				}

				// Forget about the last character of the `result`
				temp_string = result.slice(0, result.length-1);
				// Reset `result` to an empty string
				result = "";
			}

			// When the middle index is even
			else {

				for (let i=half; i<temp_string.length; i++) {
				
					// When the middle index of the string is even, we need to loop\
					// one extra time. Since this means surpassing the last string\
					// index, when we reach that iteration only add to the `result`\
					// the character that is `half` indices behind from the current\
					// index	
					if (i === temp_string.length) {
						result += temp_string[i-half];
					}

					// If we are in any other iteration add to `result` the character\
					// at the current index and the one `half` indices behind
					else {
						result += temp_string[i];
						result += temp_string[i-half];
					}
				}

				// Forget about the last character of `result`
				temp_string = result.slice(0, result.length-1);
				// Reset `result` to an empty string
				result = "";
			}
		}

		// Finally, return the result of the decryption
		return temp_string;
	}	
}



console.log("encrypt(\"This is a test!\", 0):", encrypt("This is a test!", 0));
console.log("encrypt(\"This is a test!\", 1):", encrypt("This is a test!", 1));
console.log("encrypt(\"This is a test!\", 2):", encrypt("This is a test!", 2));
console.log("encrypt(\"This is a test!\", 3):", encrypt("This is a test!", 3));
console.log("decrypt(\"hsi  etTi sats!\", 1):", decrypt("hsi  etTi sats!", 1));
console.log("decrypt(\"s eT ashi tist!\", 2):", decrypt("s eT ashi tist!", 2));
console.log("decrypt(\"hskt svr neetn!Ti aai eyitrsig\", 1):", decrypt("hskt svr neetn!Ti aai eyitrsig", 1));