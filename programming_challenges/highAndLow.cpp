// https://www.codewars.com/kata/highest-and-lowest/cpp
/*
Given a string of space-separated integers, return a string with the
largest and smallest integers in the form
	"largNum smalNum"

Example:

	highAndLow("1 2 3 4 5");  // "5 1"
	highAndLow("1 2 -3 4 5"); // "5 -3"
	highAndLow("1 9 3 4 -5"); // "9 -5"

All numbers are valid Int32.
The string will always contain at least one number.
The largest number must be the first in the return string, separating the
numbers with a single space.
*/

#include <string>
#include <sstream>
#include <vector>
#include <iostream>
using namespace std;


// Split the string and obtain a vector with each number (as strings)
vector<string> splitString (string inputString) {
	// Create a string stream using the input string
	istringstream ss(inputString);
	// Variable to hold the contents of each split in the loop
	string token;
	// Vector to contain the string splits
	vector<string> splitVector;

	// Split the input string at spaces and obtain a vector with the existing\
	// "words" and/or numbers
	while (getline(ss, token, ' ')) {
		// Append the new split to the vector
		splitVector.push_back(token);
	}

	return splitVector;
};

// Find the largest number in the vector of splits
string findMax (vector<string> strVector) {
	string maxNum = strVector[0];

	for (int i=0; i<strVector.size(); i++) {
		if (stoi(maxNum) < stoi(strVector[i])) {
			maxNum = strVector[i];
		}
	}

	return maxNum;
}

// Find the smallest number in the vector of splits
string findMin (vector<string> strVector) {
	string minNum = strVector[0];

	for (int i=0; i<strVector.size(); i++) {
		if (stoi(minNum) > stoi(strVector[i])) {
			minNum = strVector[i];
		}
	}

	return minNum;
}


// Actual challenge function
string highAndLow (string inputString) {
	vector<string> splits = splitString(inputString);
	string maxNum = findMax(splits);
	string minNum = findMin(splits);
	string result = maxNum + " " + minNum;
	return result;
}



int main () {
	string inputString = "-1 2 5 4 3";	
	string result = highAndLow(inputString);
	cout << result << endl;

	return 0;
}