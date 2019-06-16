// https://www.codewars.com/kata/valid-parentheses/javascript
/*
Write a function called `validParentheses` that takes a string of parentheses
and determines if the order of the parentheses is valid.
The function should return true if the string is balanced, and false if it's
not.

Examples:
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
*/

function validParentheses (parens){
	// Stack to contain opening parenthesis
	var stack = [];

	// If the string starts with a closing parenthesis, return false right\
	// away
	if (parens[0] === ")") {
		return false;
	}

	// Loop through the string
	for (var i = 0; i < parens.length; i++) {
		
		// If the current character is an opening parenthesis, add it to the\
		// stack (it will be kept there until we find the closing counterpart)
		if (parens[i] === "(") {
			stack.push("(");
		}
		
		// If the current character is a closing parenthesis
		else {
			
			// Then, if the stack is not empty, remove an item (that is\
			// remove one of the previously found opening parenthesis\
			// to signify that we found a match)
			if (stack.length != 0) {
				stack.pop();
			}
			// If the stack is empty, it means we came across a mismatched\
			// closing parenthesis, thus return false
			else {
				return false;
			}
		
		}
	
	}
	
	// After looping through the string, the stack must be empty
	// If it isn't, the string is not balanced
	if (stack.length != 0) {
		return false;
	}
	// Otherwise, it is balanced
	else {
		return true;
	}

}

console.log(validParentheses("()"));
console.log(validParentheses("())"));

// Another possibility would be to keep a counter. For every opening\
// parenthesis, the counter is incremented; closing parenthesis\
// decrement the counter. If the counter is ever negative, then the\
// string is unbalanced; otherwise, it is balanced

function validParenthesesV2 (parens) {
	// Counter for the balance
	var counter = 0;

	// Loop through the string. Opening parenthesis increment the balance,
	// closing ones decrement
	for (var i=0; i < parens.length; i++) {
		
		if (parens[i] == "(") {
			counter++;
		}
		
		else {
			counter--;
		}

		// If the counter ever goes below 0, then the string is unbalanced
		if (counter < 0) {
			return false;
		}
	}

	// After the loop, if the balance is null, return true; else the string\
	// is unbalanced
	if (counter === 0) {
		return true;
	}
	else {
		return false;
	}
}

console.log(validParenthesesV2("()"));
console.log(validParenthesesV2("())"));