# https://www.codewars.com/kata/57814d79a56c88e3e0000786/solutions/cpp
'''
Take every second character from an input string, then concatenate the
remaining characters to that to create an encrypted string. This operation
is done n times.
Examples:
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two functions:
encrypt(text, n)
decrypt(encryptedText, n)
Extra rules:
If the input string is empty then return an empty string.
If n is <= 0 then return the input string.
'''


def encrypt (text, n):
	if (text == ""):
		return ""
	elif (n < 0):
		return text
	else:
		# The temporary string starts as the input string
		temp_string = text

		# We need to encrypt `n` times
		for encryption in range(n):
			# Loop through every second character, then loop through every first character.
			# Then concatenate the two lists and join all items in a single string without\
			# spaces between characters
			temp_string = "".join(
				[temp_string[i] for i in range(1, len(temp_string), 2)] +
				[temp_string[i] for i in range(0, len(temp_string), 2)]
			)

		# Finally, return the encryption result
		return temp_string

def decrypt (encryptedText, n):
	if (encryptedText == ""):
		return ""
	elif (n < 0):
		return text
	else:
		# The temporary string starts as the input string
		temp_string = encryptedText
		# Variable to hold the result of each decryption
		result = ""

		# We need to decrypt `n` times
		for decryption in range(n):
			# Get the middle index of the input string
			half = int(len(temp_string) / 2)

			# When the middle index is odd
			if (len(temp_string)%2 != 0):
				# Loop through the `temp_string` string, starting at the middle\
				# and, each iteration, add to the `result` the character at the\
				# current index and the one `half` indices behind
				for i in range(half, len(temp_string), 1):
					result += temp_string[i]
					result += temp_string[i-half]
				
				# Forget about the last character of the `result`
				temp_string = result[:-1]
				# Reset `result` for the next decryption
				result = ""

			# When the middle index is even
			else:
				for i in range(half, len(temp_string)+1, 1):

					# When the middle index of the string is even, we need to loop\
					# one extra time. Since this means surpassing the last string\
					# index, when we reach that iteration only add to the `result`\
					# the character that is `half` indices behind from the current\
					# index
					if i == len(temp_string):
						result += temp_string[i-half]
					# If we are in any other iteration add to `result` the character\
					# at the current index and the one `half` indices behind
					else:
						result += temp_string[i]
						result += temp_string[i-half]

				# Forget about the last character of `result`
				temp_string = result[:-1]
				# Reset `result` for the next decryption
				result = ""

	# Finally, return the decryption result
	return temp_string




import unittest

class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(encrypt("This is a test!", 0), "This is a test!")

	def test2(self):
		self.assertEqual(encrypt("This is a test!", 1), "hsi  etTi sats!")

	def test3(self):
		self.assertEqual(encrypt("This is a test!", 2), "s eT ashi tist!")

	def test4(self):
		self.assertEqual(encrypt("This is a test!", 3), " Tah itse sits!")

	def test5(self):
		self.assertEqual(decrypt("hsi  etTi sats!", 1), "This is a test!")

	def test6(self):
		self.assertEqual(decrypt("s eT ashi tist!", 2), "This is a test!")

	def test7(self):
		self.assertEqual(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")


unittest.main()