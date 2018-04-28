// https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/javascript

/*
The input is a string 'str' of digits. Cut the string into chunks 
(a chunk here is a substring of the initial string) of size 'sz' 
(ignore the last chunk if its size is less than 'sz').

If a chunk represents an integer such as the sum of the cubes 
of its digits that is divisible by 2, reverse that chunk; otherwise 
rotate it to the left by one position. Put together these 
modified chunks and return the result as a string.

If 'sz' is <= 0 or if str is empty return "".
If 'sz' is greater (>) than the length of 'str' it is impossible 
to take a chunk of size 'sz' hence return "".
*/

function revrot(str, sz) {
    // If 'sz' is either negative, zero or bigger than the
    // length of the string then return an empty string
    if (sz <= 0 || sz > str.length) {
        return ""
    }

    // The string to be returned at the end
    var final = '';

    // Loop through 'str', in chunks of 'sz' digits
    for (let i=0; i<str.length; i+=sz){
        // Pick a new chunk
        var chunk = str.substr(i, sz);
        // If the chunk is smaller than 'sz',
        // break out of the loop because we've
        // reached the end of the number and
        // we're not interested in chunks smaller
        // than 'sz'
        if (chunk.length < sz) {
            break;
        }
        
        // Temporary variable to hold the sum of the
        // squares of the digits in chunk
        var chunk_sum = 0;
        
        // Loop through the chunk to extract the sum
        // of the squares of its digits
        for (digit of chunk) {
            chunk_sum += (parseInt(digit) * parseInt(digit));
        }
        
        // Test if the sum of the chunk's digits's squares is even
        if (chunk_sum%2 == 0) {
            // If it is, reverse the chunk (split its digits to obtain 
            // an array, reverse the array and then convert the array
            // into a single string) and add it to the final string
            final += chunk.split("").reverse().join("");
        } else {
            // If it isn't, add the chunk to the final string, with the
            // chunk's digits moved one index to the left (so the first
            // digit is now the last, the second is now the first, ...)
            final += chunk.substr(1, sz) + chunk[0];
        }
    }

    // Return the resulting string
    return final
}

console.log('revrot("1234", 0) =>', revrot("1234", 0));
console.log();
console.log('revrot("", 0) =>', revrot("", 0));
console.log();
console.log('revrot("1234", 5) =>', revrot("1234", 5));
console.log();
console.log('revrot("733049910872815764", 5) =>', revrot("733049910872815764", 5));