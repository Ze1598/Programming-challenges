// https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/javascript

/*
Write a function that will return the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in 
the input string. The input string can be assumed to contain only 
alphabets (both uppercase and lowercase) and numeric digits.

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

*/

function duplicateCount(text){
    // Lower case input
    var text = text.toLowerCase();
    // Object to hold the distinct letters and digits and
    // the number of its instances
    var letters = {};
    // How many letters/digits occur more than once
    var count = 0;

    // Loop through the input to extract the distinct
    // letters and digits and how many times they occur
    for (let i=0; i<text.length; i++) {
        if (letters.hasOwnProperty(text[i]) == false) {
            letters[text[i]] = 1;
        } else {
            letters[text[i]] += 1;
        }
    }

    // Loop through the found letters/digits to see how many
    // of them have occured more than once in the input string
    for (var key in letters) {
        if (letters[key] > 1) {
            count += 1
        }
    }

    return count
}

console.log(duplicateCount(""))
console.log()
console.log(duplicateCount("abcde"))
console.log()
console.log(duplicateCount("aabbcde"))
console.log()
console.log(duplicateCount("Indivisibilities"))