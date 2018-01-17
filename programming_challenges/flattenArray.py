# https://discuss.codecademy.com/t/challenge-flatten-an-array/218659
# Write a function, flattenArray, that when given an 2D array, flattens it into a 1D array
# Function Name: flattenArray
# Input: a 2D array
# Output: a 1D array
# Example: flattenArray([1,2,3, [4,5], 6, [7,8], 9]) => [1,2,3,4,5,6,7,8,9]

def flattenArray(arr):
    arr_ = []
    # for i in arr:
    #     print(i,type(i))
    for i in arr:
        if type(i) != type(1):
            for i2 in i:
                arr_.append(i2)
        else:
            arr_.append(i)
    return arr_
print('flattenArray([1,2,3, [4,5], 6, [7,8], 9]) =>', flattenArray([1,2,3, [4,5], 6, [7,8], 9]))

# Function Name: flattenArrayN
# Input: any array with n levels of depth, where n is an integer n>=1
# Output: a 1D array
# Example: flattenArrayN([1, 2, [3, [4, 5]], 6])) => [1, 2, 3, 4, 5, 6]
# For our intermediate challenge, the array can have multiple types: {}, [], "", undefined, null, and integers (1,2,3,...) are all valid types inside the array.


def flattenArrayN(arr):
    arr_ = []
    for i in arr:
        if type(i) is not int:
            #recursively flat 'i' if 'i' is not an integer (here we're assuming if 'i' is not an integer then it is a list)
            arr_.extend(flattenArrayN(i))
        else:
            arr_.append(i)
    return arr_
    
print('flattenArrayN([1, 2, [3, [4, 5]], 6])) =>',flattenArrayN([1, 2, [3, [4, 5]], 6]))
