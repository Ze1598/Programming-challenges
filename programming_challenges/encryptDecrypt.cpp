// https://www.codewars.com/kata/57814d79a56c88e3e0000786/solutions/cpp
/*
Take every second character from an input string, then concatenate the
remaining characters to that to create an encrypted string. This operation
is done n times.
Examples:
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two functions:
std::string encrypt(std::string text, int n)
std::string decrypt(std::string encryptedText, int n)
Extra rules:
If the input string is empty then return an empty string.
If n is <= 0 then return the input string.
*/
#include <iostream>
#include <string>
using namespace std;

string encrypt(string text, int n) {
	if (text == "") {
		return "";
	}
	else if (n < 0) {
		return text;
	}
	else {
		string temp_string = text;
		// Run the loop n times
		for (int j=0; j<n; j++) {
			// First half string
			string string_first_half = "";
			// Second half string
			string string_second_half = "";
			// Loop through the characters of the string with odd index\
			(these are added to the first half)
			for (int i=1; i<temp_string.length(); i+=2) {
				string_first_half += temp_string[i];
			}
			// Loop through the characters of the string with even index\
			// (these are added to the second half)
			for (int i=0; i<temp_string.length(); i+=2) {
				string_second_half += temp_string[i];				
			}
			// When this division ends, update temp_string to the concatenation\
			// of the first and second halves
			temp_string = string_first_half + string_second_half; 
		}
		return temp_string;
	}

}

string decrypt(string encryptedText, int n) {
	if (encryptedText == "") {
		return "";
	}
	else if (n < 0) {
		return encryptedText;
	}
	else {
		string temp_string = encryptedText;
		string result;
		// Run the loop n times
		for (int j=0; j<n; j++) {
			// We'll use the center of the string as our point of reference
			int half = temp_string.length() / 2;
			// If the string has odd length, then we'll loop from the center\
			// of the string until the end (and we'll the delete the last\
			// resulting character at the end)
			if (temp_string.length()%2 != 0) {
				for (int i=half; i<temp_string.length(); i++) {
					// Always add to the resulting string the character at the\
					// currend index, followed by the character that is `half`\
					// indices behind
					result += temp_string[i];
					result += temp_string[i-half];
				}
				// Delete the last character from the result
				result.erase(result.length()-1, 1);
				// The string for the next iteration will be the current result\
				// (the output of this inner loop is the input for the next\
				// iteration of the outer loop)
				temp_string = result;
				// Reset the result to an empty string
				result = "";
			}
			// If the string has even length, then we'll loop from the center\
			// of the string until the end plus one index (and we'll the\
			// delete the last two resulting characters at the end)
			else {
				for (int i=half; i<temp_string.length()+1; i++) {
					// Always add to the resulting string the character at the\
					// currend index, followed by the character that is `half`\
					// indices behind					
					result += temp_string[i];
					result += temp_string[i-half];
				}

				// Delete the last two characters from the result
				result.erase(result.length()-2, 2);
				// The string for the next iteration will be the current result\
				// (the output of this inner loop is the input for the next\
				// iteration of the outer loop)
				temp_string = result;
				// Reset the result to an empty string
				result = "";
			}
		}
		return temp_string;
	}
}


int main() {
	cout << "encrypt(\"This is a test!\", 0) => " << encrypt("This is a test!", 0) << "\n";
	cout << "encrypt(\"This is a test!\", 1) => " << encrypt("This is a test!", 1) << "\n";
	cout << "encrypt(\"This is a test!\", 2) => " << encrypt("This is a test!", 2) << "\n";
	cout << "encrypt(\"This is a test!\", 3) => " << encrypt("This is a test!", 3) << "\n";
	cout << "decrypt(\"hsi  etTi sats!\", 1) => " << decrypt("hsi  etTi sats!", 1) << "\n";
	cout << "decrypt(\"s eT ashi tist!\", 2) => " << decrypt("s eT ashi tist!", 2) << "\n";
	cout << "decrypt(\"hskt svr neetn!Ti aai eyitrsig\", 1) => " << decrypt("hskt svr neetn!Ti aai eyitrsig", 1) << "\n";
}