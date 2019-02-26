# https://www.codewars.com/kata/split-strings/train/python

'''
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the 
missing second character of the final pair with an underscore ('_').

Examples:
string_pairs('abc') #should return ['ab', 'c_']
string_pairs('abcdef') #should return ['ab', 'cd', 'ef']
'''

def string_pairs(string):
    return [string[i] + string[i+1] for i in range(0,len(string), 2)] if len(string)%2==0 else [string[i] + string[i+1] for i in range(0,len(string)-1, 2)] + [string[-1]+'_']


import unittest

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(string_pairs('abcd'), ['ab', 'cd'])

    def test2(self):
        self.assertEqual(string_pairs('abc'), ['ab', 'c_'])
    
    def test3(self):
        self.assertEqual(string_pairs('abcdef'), ['ab', 'cd', 'ef'])

if __name__ == "__main__":
    unittest.main()