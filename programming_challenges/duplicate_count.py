# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/javascript

'''
Write a function that will return the count of distinct case-insensitive 
alphabetic characters and numeric digits that occur more than once in 
the input string. The input string can be assumed to contain only 
alphabets (both uppercase and lowercase) and numeric digits.

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''

def duplicate_count(text):
    # Mapping of distinct letters/digits and its\
    # occurrences
    letters = {}

    # Loop through the input in lower case
    for i in text.lower():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
            
    # Return how many letters/digits occur more than once
    return [letters[i] > 1 for i in letters].count(True)

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(duplicate_count("abcde"), 0)
    def test2(self):
        self.assertEqual(duplicate_count("abcdea"), 1)
    def test3(self):
        self.assertEqual(duplicate_count("indivisibility"), 1)
    
if __name__ == "__main__":
    unittest.main()