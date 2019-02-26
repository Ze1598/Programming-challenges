# https://www.codewars.com/kata/did-i-finish-my-sudoku/train/python

'''
Write a function done_or_not that receives a sudoku board as input. 
If the board is valid return 'Finished!', otherwise return 'Try again!'.
'''

def sudoku_complete(board):
    '''
    Test each row;
    Test each column;
    Test each square;
    If it passes all three tests, then it is complete;
    If it fails one of the tests, immediately returns the result;
    '''

    # Check if each row contains 9 different numbers
    for row in board:
        if len(set(row)) != 9:
            return 'Try again!'
    
    # Check if each column contains 9 different numbers
    for i in range(9):
        if len(set([board[j][i] for j in range(9)])) != 9:
            return 'Try again!'

    # Scrape the 9 numbers present in each square (3x3)
    # Do it by scraping each row of each square by looping\
    # through each row of the board. From each row of the\
    # board we scrape 3 sets of rows
    squares = [ [], [], [] ]
    # Counter to keep track of which list to append to
    z = 0
    # Loop through the rows of the board
    for row in range(9):
        # Each time we finish scraping 3 rows, it means 3\
        # squares were completed, thus append 3 new empty\
        # lists which will hold the next 3 squares
        if row in [3,6]:
            squares.append([])
            squares.append([])
            squares.append([])
            # Also update the counter so it will focus on the 3\
            # newly created lists
            z = row
        # In each row of the board, scrape 3 consecutive numbers at\
        # a time (each set of 3 corresponds to a different square)
        for j in [0,3,6]:
            squares[z].append(board[row][j:j+3])
            # Increment the counter so we can append the numbers to the
            # corret square
            z += 1
        # This decrement makes it so the counter stays focused in the 3\
        # lists that represent the squares currently being scraped
        z -= 3

    # Now verify if each square contains 9 different numbers
    for i in range(9):
        if len(set(squares[i][0] + squares[i][1] + squares[i][2])) != 9:
            return 'Try again!'
            
    # If it passed all 3 tests, then the board is correct
    return 'Finished!'

import unittest

a = [ [1, 3, 2, 5, 7, 9, 4, 6, 8]
    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
    ,[8, 7, 9, 6, 4, 2, 1, 3, 5] ]

b = [ [1, 3, 2, 5, 7, 9, 4, 6, 8]
    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
    ,[8, 7, 9, 6, 4, 2, 1, 5, 3] ]

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(sudoku_complete(a), 'Try again!')
    
    def test2(self):
        self.assertEqual(sudoku_complete(b), 'Finished!')

if __name__ == '__main__':
    unittest.main()