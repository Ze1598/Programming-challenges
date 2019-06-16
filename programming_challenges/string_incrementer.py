# https://www.codewars.com/kata/string-incrementer/python
'''
Write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number, the number 1 should be appended to the
new string.
If the number has leading zeros, the amount of digits should be considered.

Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
'''

import re

def string_incremeter (string):
	# Empty string
	if string == "":
		return "1"
	
	# String contains only letters, thus just prefix it with a one
	elif string.isalpha() == True:
		return string + "1"
	
	# The string does not contain only letters, but its last character\
	# is not a digit (thus it counts as if it contained only letters)
	elif string[-1].isdigit() == False:
		return string + "1"
	
	# The string does not contain only letters and its last character\
	# is a number (confirms that at least one digit is at the end\
	# of the string and not somewhere else)
	elif string[-1].isdigit() == True:
		# We are looking for as many (one or more) digits the string has at\
		# the end
		regex = r"[0-9]+$"
		# Search for the regular expression in the input string
		string_match = re.search(regex, string)
		# Index of the first character matched (used to remove the original\
		# number when creating the incremented string)
		match_start = string_match.start()
		# Extract the number found (as a string)
		extract_num = string_match.group(0)

		# If the number doesn't have trailing zeroes, simply increment it\
		# by one and suffix it to the string (removing the original number\
		# from the string)
		if len(extract_num) == len(str(int(extract_num))):
			return string[:match_start] + str(int(extract_num)+1)

		# The number has trailing zeroes
		else:

			# Increment the extracted number
			inc_num = int(extract_num) + 1
			# If, after being incremented, the number has the same length as the\
			# original number with trailing zeroes, suffix it to the string with no\
			# further changes (without the original number) (e.g., "099" -> 99 -> 100)
			if len(str(inc_num)) == len(extract_num):
				return string[:match_start] + str(inc_num)

			# If the incremented number is missing trailing zeroes, add the necessary\
			# zeroes and then add the number to the string
			else:
				# Calculate the zeroes needed
				needed_zeroes = len(extract_num) - len(str(inc_num))
				# Prefix the incremented number with the necessary zeroes (as a string)
				num_to_add = "0" * needed_zeroes + str(inc_num)
				# Finally, create the incremented string
				return string[:match_start] + num_to_add


if __name__ == "__main__":
	strings = ["foo", "foobar001", "foobar1", "foobar00", "foo099", ""]
	print("Increment strings:")
	for s in strings:
		print(f"{s} => {string_incremeter(s)}")


# ---------------------------------------------------------------------------------

# Alternate solution (https://www.codewars.com/kata/54a91a4883a7de5d7800009c/solutions/python)
def increment_string(strng):
	# Strip any trailing digits from the string
	head = strng.rstrip('0123456789')
	# Now extract the target number (the striped trailing digits)
	tail = strng[len(head):]
	# If `tail` is an empty string, it means that the string has no trailing number,\
	# thus simply suffix it with a one
	if tail == "":
		return strng+"1"
	# Otherwise, increment the string: the `head` (the string without the trailing\
	# number) and the incremented number (increment the number and then add as many\
	# leading zeroes as needed to have the original number of digits)
	return head + str(int(tail) + 1).zfill(len(tail))