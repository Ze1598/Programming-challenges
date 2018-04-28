# http://www.codewars.com/kata/range-extraction/python

import unittest
from random import randint

def range_extraction(args):
    # The slice start
    i = 0
    # The slice end
    j = i + 3
    # List to containg the formatted numbers
    elements = []

    while True:

        # If the slice contains only consecutive numbers
        if args[i:j] == list(range(args[i], args[j-1]+1)) and j <= len(args):
            # Next iteration try the slice with one more number (if there are more)
            if j+1 <= len(args):
                j += 1

            # If there are no more numbers, take care of these remaining numbers
            else:
                # If there's at least three of them, then it means we can simply add\
                # them as a single range formatting
                if len(args)-i > 2:
                    elements.append(str(args[i]) + '-' + str(args[j-1]))
                
                # Otherwise, there are two numbers remanining. Append them separately
                else:
                    elements.append(str(args[i]))
                    elements.append(str(args[i+1]))
                break

        # If the slice doesn't contain just consecutive numbers
        else:
            # If the slice had only consecutive numbers until the addition of the last\
            # number, add the slice without that last number.
            # Then the next slice to be tested starts where the newly added one ended
            if args[i:j-1] == list(range(args[i], args[j-2]+1)):
                # If there's at least 3 numbers left in the list and the current slice\
                # has more than 2 numbers, then add the slice to the results
                if len(args)-i > 2 and len(args[i:j-1]) > 2:
                    elements.append(str(args[i]) + '-' + str(args[j-2]))
                # Else, just append the two leftover numbers
                else:
                    elements.append(str(args[i]))
                    elements.append(str(args[i+1]))
                # If we are at the end of the list, stop the loop
                if j == len(args):
                    if str(args[-1]) not in elements[-1]:
                        elements.append(str(args[-1]))
                    break
                
                # Adjust the begin and end of the next slice
                i = j-1
                j = i + 3
                if j > len(args):
                    j = len(args)
            
            # If it didn't contain just consecutive numbers anyway, add only the first\
            # number of the slice to the results.
            # Then the next slice starts at the number that followed the added number.
            else:
                elements.append(str(args[i]))
                i += 1
                j = i + 3
                # If there's not enough numbers to create a 3-numbers slice, create\
                # one with as many numbers as possible between the current position\
                # in the list and the end of it
                if j > len(args):
                    if len(args) -i == 2:
                        elements.append(str(args[-2]))
                        elements.append(str(args[-1]))
                        break
                    elif len(args) -i == 1:
                        elements.append(str(args[-1]))
                        break
                    j = len(args)

        # If we are trying to start a slice at the end of the list, just stop the loop
        if i == len(args):
            break

    return ','.join(elements)


class Tests(unittest.TestCase):    

    def test1(self):
        self.assertEqual(range_extraction([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')

    def test2(self):
        self.assertEqual(range_extraction([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')

if __name__ == '__main__':
    unittest.main()
    test1 = sorted({randint(1, 35)*-1 for i in range(15)})
    print(f'range_extraction(test1) =>', range_extraction(test1))