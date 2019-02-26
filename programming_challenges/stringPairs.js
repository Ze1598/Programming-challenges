// https://www.codewars.com/kata/split-strings/train/javascript

/*
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the 
missing second character of the final pair with an underscore ('_').

Examples:
stringPairs('abc') // should return ['ab', 'c_']
stringPairs('abcdef') // should return ['ab', 'cd', 'ef']
*/

function stringPairs(str) {
    // Array with the solution
    var returnArray = []

    // Test if the string has odd or even length
    if (str.length%2 == 0) {
        // If it has even length, we simply push pairs of
        // characters to the array by looping through the string,
        // two characters at a time
        for (var i=0; i<str.length; i+=2) {
            returnArray.push(str[i]+str[i+1])
        }
    } else {
        // If it has odd length, we loop through the string two
        // characters at a time, until the second last character.
        // We push the pairs of characters to the array and then
        // push the last character of the string separately with 
        // an underscore as the second character of the pair
        for (var i=0; i<(str.length-1); i+=2) {
            returnArray.push(str[i]+str[i+1])
        }
        returnArray.push(str[str.length-1]+'_')
    }

    // Finally, return the resulting array
    return returnArray
}

console.log(stringPairs('abcd'))
console.log(stringPairs('abc'))