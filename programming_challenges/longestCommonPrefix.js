// https://leetcode.com/problems/longest-common-prefix/
/*
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
*/

function longestCommonPrefix (strs) {
	// String to hold the currently longest prefix found (defaults to\
	// an empty string)
	let prefix = "";

	// If the input array is empty, just return the empty string
	if (strs.length === 0) {
		return prefix;
	}

	// Loop through the first word (we don't need to loop further than the\
	// length of this word, because the longest common prefix can only be\
	// as long as or shorter than this word)
	for (let i=0; i<strs[0].length; i++) {
		// Save the current character
		const character = strs[0][i];
		
		// Now loop through the array of strings to compare the character\
		// at the current index in all strings with the "original" character
		for (let j=0; j<strs.length; j++) {
			// If the character at the current index of the current string\
			// is different from that of the first word, then return the\
			// prefix as is because it will not be any longer
			if (strs[j][i] !== character) {
				return prefix;
			}
		}

		// If, after looking through all strings, we have found the same\
		// character in all strings, then append that character to the\
		// prefix
		prefix += character;
	
	}

	return prefix;
}


var example1 = ["flower", "flow", "flight"];
console.log( "Longest common prefix (example 1): " + longestCommonPrefix(example1) )

var example2 = ["dog", "racecar", "car"];
console.log( "Longest common prefix (example 2): " + longestCommonPrefix(example2) )

var example3 = [];
console.log( "Longest common prefix (example 3): " + longestCommonPrefix(example3) )