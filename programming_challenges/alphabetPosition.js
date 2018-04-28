// https://www.codewars.com/kata/replace-with-alphabet-position/train/python

/*
Given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
Note the alphabet's index is one-based, that is "a" is 1, "b" is 2 and so on.

As an example:
alphabetPosition("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.
*/


function alphabetPosition(text) {
    // Lower case alphabet
    var alphabet = 'abcdefghijklmnopqrstuvwxyz';
    // String to be returned
    var string = '';
    // Convert the input to lower case
    var text = text.toLowerCase()
    // Loop through the input string
    for (let i=0; i<text.length; i++) {
        // If the character is a letter...
        if (alphabet.indexOf(text[i]) != -1) {
            // ... add it to the created string
            string += (alphabet.indexOf(text[i]) + 1).toString() + ' ';
        }
    }

    // Return the created string, but without its last character (a space)
    return string.substring(0, string.length-1);
}


console.log("The sunset sets at twelve o' clock. =>", alphabetPosition("The sunset sets at twelve o' clock."));
console.log();
console.log("The narwhal bacons at midnight. =>", alphabetPosition("The narwhal bacons at midnight."));