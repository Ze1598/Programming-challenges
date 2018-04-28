// https://www.codewars.com/kata/53368a47e38700bd8300030d/solutions/javascript
// Given: an array containing hashes of names
// Return: a string formatted as a list of names separated by commas except\
// for the last two names, which should be separated by an ampersand.

function formatNames(names){
    // Array to hold only the names of the hash
    var names_ = [];

    // Loop through the input to extract the names\
    // and save them in the created array
    for (let i=0; i<names.length; i++) {
        names_.push(names[i]['name']);
    }
	
	// If there's no names return an empty string
    if (names.length == 0) {
		return ''
	// If there's 1 name, return that name
    } else if (names.length == 1) {
		return names_[0]
	// If there's 2 names, return a single string with\
	// the names separated by an ampersand
    } else if (names.length == 2) {
		return names_.join(' & ')
	// If there's multiple names, return a single string\
	// with the names separated by spaces, except for the\
	// last name, which is separated by an ampersand
    } else {
        return names_.slice(0, names_.length-1).join(', ') + ` & ${names_[names_.length-1]}`
    }

}

console.log(list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ]))
console.log(list([ {name: 'Bart'}, {name: 'Lisa'}]))
console.log(list([ {name: 'Bart'}]))
console.log(list([]))