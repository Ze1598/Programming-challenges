# https://www.codewars.com/kata/persistent-bugger/train/python

'''
Write a function, mult_persis, that takes in a positive parameter 
'n' and returns its multiplicative persistence, which is the 
number of times you must multiply the digits in 'n' until you 
reach a single digit.

    mult_persis(39) => 3 Because 3*9 = 27, 2*7 = 14, 1*4=4
and 4 has only one digit.

    mult_persis(999) => 4 Because 9*9*9 = 729, 7*2*9 = 126,
1*2*6 = 12, and finally 1*2 = 2.

    mult_persis(4) => 0 Because 4 is already a one-digit number.
'''

def mult_persis(n):
    # Counter for the multiplicative persistence
    multip = 0

    # Keep looping while the number has more than 1 digit
    while len(str(n)) > 1:

        # Temporary variable to hold the value of the\ 
        # digits multiplication
        new_n = 1

        # Loop through the current number to find the\
        # multiplication product
        for digit in str(n):
            new_n *= int(digit)
        
        # Increment the multiplicative persistence because we\
        # multiplied the digits
        multip += 1
        # The number is now the product of the multiplication
        n = new_n

    return multip


import unittest

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(mult_persis(9999), 3)

    def test2(self):
        self.assertEqual(mult_persis(999), 4)
    
    def test3(self):
        self.assertEqual(mult_persis(99), 2)
    
    def test4(self):
        self.assertEqual(mult_persis(39), 3)
    
    def test5(self):
        self.assertEqual(mult_persis(4), 0)

if __name__ == "__main__":
    unittest.main()