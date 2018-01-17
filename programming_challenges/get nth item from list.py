# Write a function, getX, that given an integer x and a list returns the Xth number if the list was in sorted order.
# Function Name: getX
# Input: An integer, x, and an unsorted list of integers
# Output: The integer corresponding to the Xth number in the sorted list
# Example: getX(2, [5,10,-3,7,9]) => 5
# getX(4, [5,10,-3,7,9]) => 9
# Note that this assumes the first number is position 1 not 0.

def getX(x, num_list):
#the following chunk of code is used to sort the num_list in ascending order, the result is sorted_num_list; this is equivalent to sorted(num_list)
    sorted_num_list = []
    while num_list:
        min_num = float('+inf')
        for num in num_list:
            if num < min_num:
                min_num = num
        sorted_num_list.append(min_num)
        num_list.remove(min_num)
    
    #to find the xth number in the list i use a count variable, starting at 1, since the x variable will also start at 1 rather than 0
    count = 1
    
    #now simply loop through sorted_num_list to find the number corresponding to the index x
    for num in sorted_num_list:
        if count == x:
            return num
        count += 1
    #created an else just in case the index given is out of range
    else:
        return 'The index you chose doesn\'t exist in the given list.'

print('getX(2, [5,10,-3,7,9]) =>', getX(2, [5,10,-3,7,9]))
print('getX(4, [5,10,-3,7,9]) =>', getX(4, [5,10,-3,7,9]))
print('getX(4, [5,10,-3,7,9]) =>', getX(6, [5,10,-3,7,9]))
    