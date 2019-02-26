# https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/

'''
Given two strings of letters, determine whether the second 
can be made from the first by removing one letter. The 
remaining letters must stay in the same order.

Examples:
word_funnel("leave", "eave") => True
word_funnel("reset", "rest") => True
word_funnel("dragoon", "dragon") => True
word_funnel("eave", "leave") => False
word_funnel("sleet", "lets") => False
word_funnel("skiff", "ski") => False
'''


import unittest


def word_funnel(word1, word2):
	# Loop through the indexes of word1
	for i in range(len(word1)):
		# Then iteratively remove a letter and check\
		# if word1 is equal to word2 that way. If it\
		# is return True immediately
		if (word1[:i] + word1[i+1:]) == word2:
			return True
	# If the loop reached the else clause, it means the\
	# words were never equal, thus return False
	else:
		return False


def word_funnel_bonus(word1):
	'''
	Given a string, find all words from a list
	of words that can be made by removing one 
	letter from the string. 
	If there are two possible letters you can 
	remove to make the same word, only count 
	it once. 
	Ordering of the output words doesn't matter.

	Examples:
	word_funnel_bonus("dragoon") => ["dragon"]
	word_funnel_bonus("boats") => ["oats", "bats", "bots", "boas", "boat"]
	word_funnel_bonus("affidavit") => []
	'''

	with open("english_words_list.txt") as f:
		# Create a list of all the words in the .txt file
		read_list = list(f.read().split('\n'))
		# We'll use only the words that have the same\
		# starting letter as the input word, or at\
		# least the same starting letter as the second\
		# letter of the input word
		words_list = [word for word in read_list if ((word[0] == word1[0]) or (word[0] == word1[1]))]

	# List to hold the word matches
	matches = []

	# Loop through the indexes of the input word
	for i in range(len(word1)):
		# Remove a letter of the word
		temp_word = word1[:i] + word1[i+1:]
		# If the word is in the list word and it has not found\
		# as a match before, add it to the list of matches 
		if (temp_word in words_list) and (temp_word not in matches):
			matches.append(temp_word)

	return matches



class Tests(unittest.TestCase):
	def test1(self):
		self.assertEqual(word_funnel("leave", "eave"), True)

	def test2(self):
		self.assertEqual(word_funnel("reset", "rest"), True)

	def test3(self):
		self.assertEqual(word_funnel("dragoon", "dragon"), True)

	def test4(self):
		self.assertEqual(word_funnel("eave", "leave"), False)

	def test5(self):
		self.assertEqual(word_funnel("sleet", "lets"), False)

	def test6(self):
		self.assertEqual(word_funnel("skiff", "ski"), False)

	def test7(self):
		self.assertEqual(word_funnel_bonus("dragoon"), ["dragon"])

	def test8(self):
		self.assertEqual(word_funnel_bonus("boats"), ["oats", "bats", "bots", "boas", "boat"])

	def test9(self):
		self.assertEqual(word_funnel_bonus("affidavit"), [])


if __name__ == "__main__":
    unittest.main()