// https://www.codewars.com/kata/persistent-bugger/train/javascript

/*
Write a function, multPersis, that takes in a positive parameter 
'n' and returns its multiplicative persistence, which is the 
number of times you must multiply the digits in 'n' until you 
reach a single digit.

    multPersis(39) => 3 Because 3*9 = 27, 2*7 = 14, 1*4=4
and 4 has only one digit.

    multPersis(999) => 4 Because 9*9*9 = 729, 7*2*9 = 126,
1*2*6 = 12, and finally 1*2 = 2.

    multPersis(4) => 0 Because 4 is already a one-digit number.
*/

function multPersis(n) {
    // Counter for the multiplicative persistence
    var multip = 0;
    // Parse n to a string to simplify operations
    n = n.toString()

    // Loop while n has more than 1 digit
    while (n.length > 1) {
        
        // Temporary variable to hold the value of the\ 
        // digits multiplication
        var new_n = 1;

        // Loop through the current number to find the\
        // multiplication product
        for (var i=0; i<n.length; i++) {
            new_n *= parseInt(n[i]);
        }

        // The loop ran, so increment the multiplicative\
        // persistence by 1
        multip ++;
        // n will now be the result of the latest multiplication
        n = new_n.toString();
    }

    return multip
}

console.log('multPersis(9999) =>', multPersis(9999))
console.log('multPersis(999) =>', multPersis(999))
console.log('multPersis(39) =>', multPersis(39))
