#This program calculates the hourglass sum for every hourglass in the list 'arr' and returns the maximum sum
#The list is set to be of size 6 by 6
#The values in each list are randomised values in the range 0 to 9 inclusive
#An hourglass is composed by 7 cells:
'''A B C
     D
   E F G'''
from random import randint

def find_max_hglass(arr):
    #List to hold all the hourglass sums found for 'arr'
    hglass_sums = []
    #We don't need to look for hourglasses that start in the last and second-last rows
    for row in range(len(arr)-2):
        #We don't need to look for hourglasses that start in the last and second-last columns
        for column in range(len(arr)-2):
            #The sum for each hourglass is the sum of the numbers at the coordinates relative to the current hourglass, starting with the top\
            #left coordinate as point of reference:\ 
            #top left plus the two following numbers in the same row: (row, column) + (row, column+1) + (row, column+2)
            #the number in the following row, in the following column: (row+1, column+1)
            #the numbers in the row 'row+2', in the same columns as the ones in row 'row': (row+2, column) + (row+2, column+1) + (row+2, column+2)
            hglass_sum = arr[row][column] + arr[row][column+1] + arr[row][column+2] + arr[row+1][column+1] + arr[row+2][column] + arr[row+2][column+1] + arr[row+2][column+2]
            hglass_sums.append(hglass_sum)
    return max(hglass_sums)

arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
for row in arr: print(row)
print('The maximum hourglass sum found is', find_max_hglass(arr),'\n')

#Create three randomized lists and calculate their hourglass sums
for i in range(3):
    arr = []
    for i2 in range(6):
        arr_temp = []
        for i3 in range(6):
            arr_temp.append(randint(0,9))
        arr.append(arr_temp)
    for row in arr: print(row)
    print('The maximum hourglass sum found is', find_max_hglass(arr),'\n')