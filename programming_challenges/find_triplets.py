'''
Find a Pythagorean Triple whose sum equals the integer given as input.
A Pythagorean Triple is a set of integers a, b and c such that
a^2 + b^2 = c^2.
For example, 3, 4 and 5 are a Pythagorean Triple because
3^2 + 4^2 = 5^2 <=> 9 + 16 = 25 <=> 25 = 25.
'''

def find_triplets (target):

	# We won't test values larger than half of the target
	upper_limit = target // 2
	# Test all the possible values for the first number (any number\
	# between 1 and the upper limit)
	for a in range(1, upper_limit):
		# Test all the possible values for the second number (any number\
		# between the first value and the upper limit)
		for b in range(a, upper_limit):
			# We have picked values for the first two numbers; the third number\
			# is the result of subtracting those two numbers from the target
			c = target - a - b
			# Sum the square of the first number to the square of the second
			a_b = a**2 + b**2
			# If the sum of the first two numbers squared equals the third number\
			# squared, then we found a valid triplet
			if (a_b == c**2):
				return (a, b, c)
	# If the loop has reached this point, then it means it has tested all the possible\
	# values and found zero valid triplets
	else:
		return None


for t in [12, 40, 4]:
	print( find_triplets(t) )