# https://www.codewars.com/kata/replace-with-alphabet-position/train/python

'''
Given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.
Note the alphabet's index is one-based, that is "a" is 1, "b" is 2 and so on.

As an example:
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.
'''

def alphabet_position(text):
    # Lower case alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # String to be returned
    string = ''

    # Loop through the input, in lower case
    for char in text.lower():
        # If the character is a letter, add the\
        # the position of that letter in the\
        # alphabet to the string
        if char in alphabet:
            string += str(alphabet.index(char)+1) + ' '
    
    # Return the created string (don't return the last\
    # character because it is a space)
    return string[:len(string)-1]

    # One-liner (requires the 'alphabet' string though)
    # return " ".join([str('abcdefghijklmnopqrstuvwxyz'.index(char)+1) for char in text.lower() if char in 'abcdefghijklmnopqrstuvwxyz'])


import unittest

class TestCases(unittest.TestCase):
    def test1(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
    
    def test2(self):
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

if __name__ == '__main__':
    unittest.main()