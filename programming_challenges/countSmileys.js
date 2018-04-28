// https://www.codewars.com/kata/583203e6eb35d7980400002a/train/javascript

/*
Given an array (arr), return the total number of smiling faces.

Rules for a smiling face:
	-Each smiley face must contain a valid pair of eyes. Eyes can be 
marked as ':' or ';'.
	-A smiley face can have a nose but it does not have to. Valid 
characters for a nose are '-' or '~'.
	-Every smiling face must have a smiling mouth that should be 
marked with either ')' or 'D'.

No additional characters are allowed except for those mentioned.

Valid smiley face examples:
:)  :D  ;-D :~)

Invalid smiley faces:
;(  :>  :}  :] 
*/


function countSmileys(arr) {
    // regex pattern
    var pattern = new RegExp('[:;]{1}[-~]?[)D]{1}', 'g');
    // Turn the input array into a single string
    var string = arr.join('');
    /* Retrieve the matches of matching the regex pattern
    against the input (returns an array of matches if 
    there was at least 1 match, else returns null) */
    var matches = string.match(pattern);
    /* Return the number (length) of matches (in case there
    were no matches return zero directly, since we can't
    acess the length of null) */
    return matches ? matches.length : 0

    // One-liner
    // return arr.join('').match(RegExp('[:;]{1}[-~]?[)D]{1}', 'g')) ? arr.join('').match(RegExp('[:;]{1}[-~]?[)D]{1}', 'g')).length : 0
}

console.log(countSmileys([]));
console.log(countSmileys([':D',':~)',';~D',':)']));
console.log(countSmileys([':)',':(',':D',':O',':;']));
console.log(countSmileys([';]', ':[', ';*', ':$', ';-D']));