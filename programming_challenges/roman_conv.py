# https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python


import unittest

def roman_conv(roman):
    '''Convert a roman numeral to a base 10 integer.'''
    
    # The conversion table
    conv = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    # The value of the roman number's index being tested (starts at zero)
    i = 0
    # The numerical value of the conversion
    number = 0
    
    # Keep looping until we break out of the loop due to 'i' being equal or\
    # bigger than the length of the roman number.
    while True:
        # If we are not going to test the last letter of the roman number and\
        # the current letter's value is lower than the folllowing letter,\
        # then the value to be added is the difference between the following\
        # and the current letter's values.
        # Also increment 'i' by 2 since the following letter won't need to be\
        # converted.
        if (i != len(roman)-1) and (conv[roman[i]] < conv[roman[i+1]]):
            number += (conv[roman[i+1]] - conv[roman[i]])
            i += 2
        # Else, do a direct conversion and increment 'i' by 1 to advance to the\
        # next letter
        else:
            number += conv[roman[i]]
            i += 1

        # If now 'i' is equal to or bigger than the length of the input number,\
        # break out of the loop to return the result
        if i >= len(roman):
            break

    return number

def roman_conv2(roman):
    '''An alternative I thought of.'''
    
    # The roman letters and their corresponding numerical values
    conv = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    # The numerical value of the conversion
    number = 0
    # The value of the latest letter tested
    previous = 0

    # Loop through a list where each item is a letter from the input\
    # value, where the first item is the first letter, the second\
    # value the second letter and so on (''.join(list(roman)) == roman)
    for letter in list(roman):
        # Add the numerical value of the letter to the result
        number += conv[letter]
        # As we loop through the roman number the values of the letters\
        # should always decrease, so if there's a case where it\
        # increases, subtract the lower value twice from the result\
        # (twice, one time for the actual subtraction it represents,\
        # and a second time to subtract its initial addition)
        if previous < conv[letter]:
            number -= (previous*2)
        # Before moving on to the next letter, save the value of this letter
        previous = conv[letter]
    
    return number
        

class Tests(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(roman_conv('MCMXC'), 1990)
    def test2(self):
        self.assertEqual(roman_conv('MMVIII'), 2008)
    def test3(self):
        self.assertEqual(roman_conv('MDCLXVI'), 1666)

    def test1_(self):
        self.assertEqual(roman_conv('MCMXC'), roman_conv2('MCMXC'))
    def test2_(self):
        self.assertEqual(roman_conv('MMVIII'), roman_conv2('MMVIII'))
    def test3_(self):
        self.assertEqual(roman_conv('MDCLXVI'), roman_conv2('MDCLXVI'))
        
if __name__ == "__main__":
    unittest.main()