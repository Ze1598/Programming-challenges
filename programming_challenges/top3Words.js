// https://www.codewars.com/kata/most-frequently-used-words-in-a-text/python

/*
Write a function that, given a string of text (possibly with punctuation and
line-breaks), returns an array of the top-3 most occurring words, in 
descending order of the number of occurrences.

Assumptions:
    A word is a string of letters (A to Z) optionally containing one or more 
apostrophes (') in ASCII.
    Matches should be case-insensitive, and the words in the result should 
be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 
or top-1 words should be returned, or an empty array if a text contains no 
words.
*/

function top3Words (text) {

	// Clean the string

	// Create a Regular Expression that removes all instances\
	// of the following punctuation
    var re = new RegExp("[\\[\\]?*|;&_:<>%$§+|{}\\\\()@.,/]", 'g')
    text = text.replace(re, " ")
    // Separately remove triple primes
	text = text.replace("'''", " ");
	// --------------------------------------------------------

	// Create an object where each key-value pair represents a unique word\
	// from the string and its frequency

	// Create an array with all the words contained in the input\
	// string (start by splitting the string at spaces) (using\
	// a lowercase version of the string)
	init_words_list = text.toLowerCase().split(' ')
	// Object to contain a mapping of each word to its frequency
	word_counts = {}

	// Count the frequencies of each word

	// Loop through the items of init_words_list, and save the\
	// frequencies of each word (non-empty strings) in word_counts
	for (let i=0; i<init_words_list.length; i++) {
		var word = init_words_list[i];
		// If the item is not an empty string and the string is not\
		// just a prime, adjust the word frequency in word_counts
        if (word.length > 0 & word != "\'") {
			if (word in word_counts) {
				word_counts[word] += 1;
			} else {
				word_counts[word] = 1
			}
		}
	}

	// -----------------------------------------------------------

	// Get the three most frequent words in a single array, ordered by
	// the frequency of the words

	// Create an array that contains the keys (words) from word_counts
	var words_list = Object.keys(word_counts)

	// Create an array to hold the 3 most frequent words
	var max_frequencies = []

	// Loop through the list of words three times, to find the one with\
	// the highest frequency. At the end of each iteration, remove the\
	// selected word from the list so that in the next iteration we can\
	// find the most frequent word relative to the updated list

	// Repeat the following loop 3 times
	for (let i=0; i<3; i++) {
		// The current most frequent word
		var max_word = ''
		// The frequency of the current most frequent word
		var freq = 0
		// The index of the current most frequent word, relative\
		// to words_list
		var index = 0
		// The current length of words_list
		var words_left = words_list.length

		// Loop through the keys in word_counts and find the\
		// current most frequent word, given that we are only\
		// checking keys that are currently in words_list
		for (let j=0; j<words_left; j++) {
			// If we found a word that is more frequent than the\
			// one we had found so far, update the following\
			// variables
			if (word_counts[words_list[j]] > freq) {
				max_word = words_list[j]
				freq = word_counts[words_list[j]]
				index = j
			}
		}

        // If the max_word is not an empty string, add it\
        // to the array of most frequent words, and remove\
        // it from the array containing the keys of word_counts
        if (max_word) {
            max_frequencies.push(max_word)
            words_list.splice(index, 1)            
        }
	}
	// ----------------------------------------------------------------

	return max_frequencies

}

console.log("top3Words('  //wont won\'t won't ') =>", top3Words("  //wont won't won't "))
console.log('------------------------------')
console.log("top3Words(\"  '''  \") =>", top3Words("  '''  "))
console.log('------------------------------')
console.log("top3Words(\"  , e   .. \") =>", top3Words("  , e   .. "))
console.log('------------------------------')
console.log("top3Words(\"e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e\") =>", top3Words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
console.log('------------------------------')
console.log("top3Words(\"  '  \") =>", top3Words("  '  "))
console.log('------------------------------')