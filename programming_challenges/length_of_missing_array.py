'''
https://www.codewars.com/kata/length-of-missing-array/train/python
Title:
	Length of missing array
Description:
	The input is a list of lists. If these lists were sorted by
	length, then their length would be sequencial, except that a
	single list is missing.
	There will always be a missing list whose length completes
	the sequence of lengths.
	Example:
	[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

	If the list of lists is None or empty, then return 0.
	If a inner list is None or empty, return 0 as well.
'''

def length_of_missing_lst (matrix):
	'''
	This method calculates what the sum should be if no list was missing and
	then subtracts what that sum is with the missing list. That difference
	is the answer.
	'''
	# If the matrix is None or empty, return 0 right away
	if matrix == None or matrix == []:
		return 0
	# Variables to hold the length of the shortest and longest\
	# inner lists
	min_len = float("inf")
	max_len = float("-inf")
	# Variable to hold the sum of all the numbers in the range\
	# [min_len, max_len]
	real_sum = 0
	# Variable to hold the sum of all lengths of the lists in the\
	# matrix
	actual_sum = 0

	# Loop through the matrix to find the sum of all its lists' lengths
	for lst in matrix:
		# If we find a list that is None or empty, return 0 right away
		if lst == None or lst == []:
			return 0
		# If the length of the current list is smaller than the shortest\
		# we've seen so far, it becomes the new shortest length
		if len(lst) < min_len:
			min_len = len(lst)
		# If the length of the current list is larger than the largest\
		# we've seen so far, it becomes the new largest length
		if len(lst) > max_len:
			max_len = len(lst)
		# Add the length of the current list to the running sum
		actual_sum += len(lst)

	# Find what the sum of all lengths of the lists in the matrix should be\
	# if no list was missing
	for i in range(min_len, max_len+1):
		real_sum += i

	# The length of the missing list is the difference between what the sum of\
	# lengths should be and what it is with one missing list
	return real_sum - actual_sum

# ----------------------------------------------------------------------------

# My own alternate solution
def length_of_missing_lst_alt (matrix):
	'''
	This method creates a list with all the lengths of the lists in the matrix.
	Then, from the range [length_shortest_list, length_largest_list], the integer
	that is not in the created list is the answer.
	'''
	# If the matrix is None or empty, return 0 right away
	if matrix == None or matrix == []:
		return 0
	# Variables to hold the length of the shortest and longest\
	# inner lists
	min_len = float("inf")
	max_len = float("-inf")
	# Variable to hold the sum of all the numbers in the range\
	# [min_len, max_len]
	real_sum = 0
	# Variable to hold the sum of all lengths of the lists in the\
	# matrix
	actual_sum = 0
	# List to hold the lengths of each list in the matrix
	lengths = []

	# Loop through the matrix to find the length of the shortest and\
	# the longest lists and the length of each list, as well as to\
	# check if any list is None or empty (if at least one is, return 0)
	for lst in matrix:
		if lst == None or lst == []:
			return 0
		if len(lst) < min_len:
			min_len = len(lst)
		if len(lst) > max_len:
			max_len = len(lst)
		lengths.append(len(lst))

	# Loop through all the integers between the length of the shortest\
	# and largest lists found: when we find the integer that doesn't\
	# have a list with a corresponding length in the matrix (i.e., the\
	# integer is not in the `lengths` list), return that integer
	for i in range(min_len, max_len):
		if i not in lengths:
			return i

# ----------------------------------------------------------------------------

def length_of_missing_lst_alt2 (matrix):
	# Sort the matrix by length of its lists
	# Alternatively, just call `sorted_lengths.sort()`
	sorted_lengths = sorted(matrix, key=lambda x: len(x))

	# Variable to hold the length of the list being looked at in the loop
	length = len(sorted_lengths[0])
	
	# Loop through all the numbers between the length of the shortest inner\
	# list and the largest: when we find an integer that doesn't an inner\
	# list of corresponding length, return that value	
	for counter in range(length, len(sorted_lengths[-1])+1):
		if (counter != length) or length == 0:
			return counter
		# We update `length` to be the length of the next inner list (use\
		# `counter` to get the next inner list so that we don't skip any inner\
		# list when we reach the missing length)
		if counter+1 < len(sorted_lengths):
			length = len(sorted_lengths[counter])


# Testing
# ----------------------------------------------------------------------------

import unittest

class Tests(unittest.TestCase):
	def test1 (self):
		self.assertEqual(length_of_missing_lst([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 3)

	def test2 (self):
		self.assertEqual(length_of_missing_lst([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 2)

	def test3 (self):
		self.assertEqual(length_of_missing_lst([[None], [None, None, None]]), 2)

	def test4 (self):
		self.assertEqual(length_of_missing_lst([['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'], ['a', 'a', 'a', 'a','a', 'a']]), 5)

	def test5 (self):
		self.assertEqual(length_of_missing_lst_alt([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 3)

	def test6 (self):
		self.assertEqual(length_of_missing_lst_alt([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 2)

	def test7 (self):
		self.assertEqual(length_of_missing_lst_alt([[None], [None, None, None]]), 2)

	def test8 (self):
		self.assertEqual(length_of_missing_lst_alt([['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'], ['a', 'a', 'a', 'a','a', 'a']]), 5)

	def test9 (self):
		self.assertEqual(length_of_missing_lst_alt2([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 3)

	def test10 (self):
		self.assertEqual(length_of_missing_lst_alt2([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 2)

	def test11 (self):
		self.assertEqual(length_of_missing_lst_alt2([[None], [None, None, None]]), 2)

	def test12 (self):
		self.assertEqual(length_of_missing_lst_alt2([['a', 'a', 'a'], ['a', 'a'], ['a', 'a', 'a', 'a'], ['a'], ['a', 'a', 'a', 'a','a', 'a']]), 5)

unittest.main()