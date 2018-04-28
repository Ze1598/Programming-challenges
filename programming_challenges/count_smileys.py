# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/javascript

'''
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
'''

import re, unittest

def count_smileys(arr):
	# We are looking for a pattern that:
		# starts with either a colon or a semi-colon;
		# is followed by a dash or a tilde (optional);
		# ends with either a closing parenthesis or a
	# capital D.
	pattern = r'[:;]{1}[-~]?[)D]{1}'
	# Turn the array of strings into a single string
	# and use the regex pattern to find the smiley faces
	return len(re.findall(pattern, ''.join(arr)))


class Test(unittest.TestCase):
	def test1(self):
		self.assertEqual(count_smileys([]), 0)
	def test2(self):
		self.assertEqual(count_smileys([':D',':~)',';~D',':)']), 4)
	def test3(self): 
		self.assertEqual(count_smileys([':)',':(',':D',':O',':;']), 2)
	def test4(self):
		self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
	def test5(self):
		self.assertEqual(count_smileys([':)', ';(', ';}', ':-D']), 2)
	def test6(self):
		self.assertEqual(count_smileys([';D', ':-(', ':-)', ';~)']), 3)

if __name__ == '__main__':
	unittest.main()