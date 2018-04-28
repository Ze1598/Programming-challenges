// https://www.codewars.com/kata/552c028c030765286c00007d/train/javascript

function iqTest(args){
    // Split the input string at spaces, so that we obtain\
    // an array with all the integers contained in that string.
    // Note at this point the integers are actually strings.
    var splits = args.split(' ');
    // Array to hold the integers in the form of actual integers.
    var numbers = []
    // Loop through the array of strings, convert the strings to\
    // integers and append (push) them to the 'numbers' array.
    for (var i=0; i<splits.length; i++) {
        numbers.push(parseInt(splits[i]));
    }

    // Counter to hold the number of even numbers in the first three\
    // integers of the array. If the counter is lower than 2 at end of\
    // loop, then it means the number in the array that is different in\ 
    // eveness is an even number; else it is odd.
    var even_count = 0;
    for (var i=0; i<3; i++){
        if (numbers[i]%2 === 0) {
            even_count += 1;
        }
    }

    // If the number we're looking for is even
    if (even_count < 2) {
        // Loop through the array of integers until we find\
        // the even number.
        for (var i=0; i<numbers.length; i++) {
            if (numbers[i]%2 == 0) {
                // Return the index of the even number in\
                // the array (here the index starts at 1,\
                // hence '+ 1').
                return numbers.indexOf(numbers[i]) + 1
            }
        }
    // Else, we're looking for an odd number
    } else {
        // Loop through the array of integers until we find\
        // the odd number.
        for (var i=0; i<numbers.length; i++) {
            if (numbers[i]%2 != 0) {
            // Return the index of the odd number in\
            // the array (here the index starts at 1,\
            // hence '+ 1').
            return numbers.indexOf(numbers[i]) + 1
            }
        }
    }
}

/*
Instead of looping a first time to check how many evens
we have on the first three integers, I could've just
looped through the array of integers once, and push
the position of each integer to an evens and odds lists,
dependant on the eveness of the number. That way, I
would just need to return the first element of the shortest
of those two lists (since the shortest one would've a single
item)
*/


console.log(iqTest("2 4 7 8 10"))
console.log(iqTest("1 2 2"))