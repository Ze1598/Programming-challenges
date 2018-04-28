# I came up with this idea after completing this challenge: https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python


import unittest

def num_roman_conv(num):
    '''Convert a base 10 integer in the inclusive range of 1 to
    3999 to a roman numeral.
    
    Args:
        num (int): The integer to be converted.
        
    Returns:
        result (str): The result of the conversion.'''
    
    # Convert the input to string
    num = str(num)

    # The conversion table
    conv = {
            '1': 'I', 
            '5': 'V', 
            '10': 'X', 
            '50': 'L', 
            '100': 'C', 
            '500': 'D', 
            '1000': 'M'
    }

    # Each digit, no matter if its in the context of units, tens,\
    # hundreds or thousands, will be converted following these formats.
    # '-' are to be replaced by Is, Xs, Cs, or Ms
    # '*' are to be replaced by Vs, Ls, or Ds
    # '/' are to be replaced by Xs, Cs or Ms 
    formats = {
            '1': '-',
            '2': '--', 
            '3': '---', 
            '4': '-*',
            '5': '*',
            '6': '*-',
            '7': '*--',
            '8': '*---',
            '9': '-/'
    }

    # String to hold the final conversion
    result = ''

    # If the number is in the thousands
    if len(num) == 4:
        # Since we are restricted to the 1-3999 range, the only possible\
        # digits for thousands are 1, 2 and 3, so simply add to the\
        # conversion the one, two or three Ms
        for i in range(int(num[0])):
            result += conv['1000']
        # Recursively call the function, now with only 3 digits
        # int() is used to remove leading zeroes.
        result += num_roman_conv(int(num[1:]))

    # For the hundreds, tens and units digits, pick the\
    # corresponding digit and make the conversion.
    # Always try to replace the 3 possible letters for each
    # digit. This way we can use the same line of code for 
    # all digits without of that magnitude without raising\
    # exceptions in case the replacement is not needed.

    # After making the conversion for that digit, recursively\
    # call this function using as input the current number without
    # the first digit, starting from the left, so that the magnitude\
    # is progressively reduced.


    # If the number is in the hundreds
    elif len(num) == 3:
        conversion = formats[num[0]].replace('-', conv['100']).replace('*', conv['500']).replace('/', conv['1000'])
        result += conversion
        # Recursively call the function, now with only 2 digits
        # int() is used to remove leading zeros
        result += num_roman_conv(int(num[1:]))

    # If the number is in the tens
    elif len(num) == 2:
        conversion = formats[num[0]].replace('-', conv['10']).replace('*', conv['50']).replace('/', conv['100'])
        result += conversion
        # Recursively call the function, now with only 1 digit
        # int() is used to remove leading zeros
        result += num_roman_conv(int(num[1:]))

    # If the number is lower than 10
    else:
        # Only convert if the digit is not zero; if it is, the zero is ignored
        if num != '0':
            conversion = formats[num[0]].replace('-', conv['1']).replace('*', conv['5']).replace('/', conv['10'])
            result += conversion
    
    return result


class Tests(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(num_roman_conv(1990), 'MCMXC')
    def test2(self):
        self.assertEqual(num_roman_conv(2008), 'MMVIII')
    def test3(self):
        self.assertEqual(num_roman_conv(1666), 'MDCLXVI')

if __name__ == "__main__":
    unittest.main()