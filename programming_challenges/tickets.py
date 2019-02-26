# https://www.codewars.com/kata/vasya-clerk/train/python

'''
There are a lot of people at the cinema box office standing in a huge 
line. Each of them has a single 100, 50 or 25 dollars bill. A movie
ticket costs 25 dollars.
Vasya is currently working as a clerk. He wants to sell a ticket to
every single person in this line. 
Can Vasya sell a ticket to each person and give the change if he 
initially has no money and sells the tickets strictly in the order 
people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the 
change with the bills he has at hand at that moment. Otherwise 
return NO.

tickets([25, 25, 50]) => YES 
tickets([25, 100]) => NO
'''

def tickets(people):
    # At first Vasya has no bills
    vasya = {'twentyfive':0, 'fifty':0, 'hundred':0}
    # Counter to move through the indexes of the 'people' list
    i = 0

    # Loop while there are people to buy tickets
    while i < len(people):
        # The change needed for this person to buy a ticket with its bill
        change = people[i] - 25

        # If the person needs change
        if change:
            # Change is 75
            if change == 75:
                # If Vasya doesn't have 50s, try to use three 25s
                if vasya['fifty'] < 1:
                    if vasya['twentyfive'] < 3:
                        return 'NO'
                    else:
                        vasya['twentyfive'] -= 3
                # If Vasya has 50s, use one and try to use one 25
                else:
                    vasya['fifty'] -= 1
                    if vasya['twentyfive'] < 1:
                        return 'NO'
                    else:
                        vasya['twentyfive'] -= 1
            
            # Change is 50
            elif change == 50:
                # If Vasya has no 50s, try to use two 25s
                if vasya['fifty'] < 1:
                    if vasya['twentyfive'] < 2:
                        return 'NO'
                    else:
                        vasya['twentyfive'] -= 2

                # If Vasya has 50s, just use one        
                else:
                    vasya['fifty'] -= 1
            
            # Change is 25
            elif change == 25:
                # Try to use one 25
                if vasya['twentyfive'] < 1:
                    return 'NO'
                else:
                    vasya['twentyfive'] -= 1

            # After giving change, Vasya receives the person's bill
            if people[i] == 25:
                vasya['twentyfive'] += 1
            elif people[i] == 50:
                vasya['fifty'] += 1
            elif people[i] == 100:
                vasya['hundred'] += 1
            
        
        # If the person doesn't need change, Vasya gains a 25 bill
        else:
            vasya['twentyfive'] += 1

        # Move on the next person
        i += 1
    
    # After selling tickets to every person, return 'YES'
    return 'YES'


import unittest

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(tickets([25, 25, 50]), 'YES')

    def test2(self):
        self.assertEqual(tickets([25, 100]), 'NO')

if __name__ == '__main__':
    unittest.main()