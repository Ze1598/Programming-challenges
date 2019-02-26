# Find the two smallest integers in a list
# Find the two biggest integers in a list
from random import randint
import unittest

# -------------------------------------------------

def two_smallest_numbers (num_list):
	"""
	Find the two smallest integers in a given non-empty list.
	The only way for a duplicate number to be considered as the two
	smallest numbers is when the first number of the list is that
	number.

	Parameters
	----------
	num_list : list
		The list of integers.

	Return
	------
	tuple
		The two smallest integers in the input list, where the first
		item is the smallest and the second is the second-smallest
		number.
	"""

	# Initalize the variables to hold the two smallest numbers\
	# (we start by picking the first element of the list for\
	# both)
	smallest, small2 = num_list[0], num_list[0]

	# Loop through the input list
	for i in range(len(num_list)):
		
		# Number being currently tested
		num = num_list[i]

		# If the number is bigger than the currently smallest\
		# number
		if (smallest < num):
			# If (smallest < num < small2) OR\
			# (num > smallest == small2)
			if (small2 > num) or (smallest == small2):
				# Then the number being tested is now the second-\
				# smallest number
				small2 = num

		# If the number is equal to or smaller than the smallest\
		# number (though the equality case is never of our interest)
		else:
			# If (num < smallest < small2) AND\
			# (num != smallest < small2)
			if (smallest < small2) and (smallest != num):
				# Then the smallest number is now the second-smallest\
				# number (the smallest number will always be updated\
				# after this clause)
				small2 = smallest

			# If the number being tested is not bigger than the\
			# smallest number, always define it as the new smallest\
			# number
			smallest = num

	# Return a tuple of the list's two smallest numbers
	return (smallest, small2)


def two_largest_numbers (num_list):
	"""
	Find the two largest integers in a given non-empty list.
	The only way for a duplicate number to be considered as the two
	largest numbers is when the first number of the list is that
	number.

	Parameters
	----------
	num_list : list
		The list of integers.

	Return
	------
	tuple
		The two largest integers in the input list, where the first
		item is the largest and the second is the second-largest
		number.
	"""

	# Initalize the variables to hold the two largest numbers\
	# (we start by picking the first element of the list for\
	# both)
	largest, large2 = num_list[0], num_list[0]

	# Loop through the input list
	for i in range(len(num_list)):

		# Number being currently tested
		num = num_list[i]

		# If the number is smaller than the currently largest\
		# number
		if (largest > num):
			# If (largest > num > large2) OR\
			# (num > largest == large2)
			if (large2 < num) or (largest == large2):
				# Then the number being currently tested is now\
				# the second-largest number
				large2 = num

		# If the number is equal to or larger than the currently\
		# largest number (though the equality case is never of our\
		# interest)
		else:

			# IF (num > largest > large2) AND\
			# (num != largest > large2)
			if (largest > large2) and (largest != num):
				# Then the largest number is now the second-largest\
				# number (the largest number will always be updated\
				# after this clause)
				large2 = largest

			# If the number is not smaller than the largest number,\
			# always assign it to be the new largest number
			largest = num

	# Return a tuple of the list's two largest numbers
	return (largest, large2)


class Tests (unittest.TestCase):

	# Tests for finding the two smallest numbers
	def test1(self):
		test_list = [3, 29, 13, 71]
		self.assertEqual(two_smallest_numbers(test_list), (3, 13))

	def test2(self):
		test_list = [97, 53, 21, 19]
		self.assertEqual(two_smallest_numbers(test_list), (19, 21))

	def test3(self):
		test_list = [3, 9, 3, 15]
		self.assertEqual(two_smallest_numbers(test_list), (3, 9))

	# -------------------------------------------------------------

	# Tests for finding the two largest numbers
	def test4(self):
		test_list = [3, 29, 13, 71]
		self.assertEqual(two_largest_numbers(test_list), (71, 29))

	def test5(self):
		test_list = [97, 53, 21, 19]
		self.assertEqual(two_largest_numbers(test_list), (97, 53))

	def test6(self):
		test_list = [3, 9, 3, 15]
		self.assertEqual(two_largest_numbers(test_list), (15, 9))

unittest.main()