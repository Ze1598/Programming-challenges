// https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/javascript
// Test if a given string is a valid IPv4

function isValidIP(str) {
 
    // Split the input on dots
    var splits = str.split('.');

    // Return false if there's more or less than 4 octets
    if (splits.length != 4) {
        return false
    }

    // Loop through the octets
    for (var i=0; i<splits.length; i++) {
        
        // If an octet is smaller than 0 or bigger than 255, return false
        if ((parseInt(splits[i]) < 0) || (parseInt(splits[i]) > 255)) {
            return false
        }

        // If an octet has leading zeros, return false.
        // To test this, check if the first digit is a zero and if the octet is not
        // zero, that is, it shouldn't have leading zeroes
        if (splits[i][0] == '0' && parseInt(splits[i]) != 0) {
            return false
        }
    }
    
    // If none of the previous tests were succesful, then it means this
    // is a valid IPv4
    return true
}

console.log(isValidIP('1.2.3.4'));
console.log(isValidIP('123.45.67.89'));
console.log(isValidIP('1.2.3'));
console.log(isValidIP('1.2.3.4.5'));
console.log(isValidIP('123.456.78.90'));
console.log(isValidIP('123.045.067.089'));
