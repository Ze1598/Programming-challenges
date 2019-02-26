/*
https://www.codewars.com/kata/length-of-missing-array/train/python
Title:
	Length of missing array
Description:
	The input is an array of arrays. If these arrays were sorted by
	length, then their length would be sequencial, except that one
	single array is missing.
	There will always be a missing element whose length completes
	the sequence of lengths.
	Example:
	[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

	If the array of arrays is None or empty, then return 0.
	If a inner array is None or empty, return 0 as well.
*/

#include <iostream>
#include <vector>
using namespace std;

int getLengthOfMissingArray(vector<vector<int>> arrayOfArrays) {
	// Number of arrays in the matrix (therefore the longest array needs to have
	// this length)
	// int numArrays = sizeof(arrayOfArrays) / sizeof(arrayOfArrays[0]);
	int numArrays = arrayOfArrays.size();
	// The sum of the length of all the in the matrix should equal this value
	int realSum = 0;
	// Variable to hold the sum of the length of all the arrays in `arrayOfArrays`
	int actualSum = 0;
	// Variables to hold the length of the shortest and longest\
	// inner lists
	int minLen = 2^31 - 1;
	int maxLen = - (2^31 - 1);

	// Loop through the matrix to find the sum of all its lists' lengths
	for (int i=0; i<numArrays; i++) {
		// The rules say we should return 0 as the answer if there's at least one\
		// empty array
		if (arrayOfArrays[i].size()==0) {
			return 0;
		}
		// Size of the array of `arrayOfArrays` at index `i`
		int arraySize = arrayOfArrays[i].size();
		// If the length of the current list is smaller than the shortest\
		// we've seen so far, it becomes the new shortest length
		if (arraySize < minLen) {
			minLen = arraySize;
		}
		// If the length of the current list is larger than the largest\
		// we've seen so far, it becomes the new largest length
		if (arraySize > maxLen) {
			maxLen = arraySize;
		}

		// Add the size of the current array to the running sum
		actualSum += arraySize;
	}

	// Actually calculate what `realSum` is
	for (int i=minLen; i<(maxLen+1); i++) {
		realSum += i;
	}

	// The answer of the length of the "missing array" is the difference between the\
	// sum of all the numbers between 1 and the numbers of arrays in `arrayOfArrays`\
	// and the sum of the length of all the arrays in the matrix
	return realSum - actualSum;
}

int main() {
	// Initialize a vector that will contains vectors of `int`s
	vector<vector<int>> sampleVector ;
	// Append a one-item vector
	sampleVector.push_back({1});
	// Append a three-item vector
	sampleVector.push_back({4, 5, 1});

	cout << getLengthOfMissingArray(sampleVector) << "\n";
}