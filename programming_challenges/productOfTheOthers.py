# Write a function, productOfTheOthers that, when given an array of n integers, replaces each number in the array with the product of all the numbers in the array except the number itself.
# for example, when given the array [1,2,3,4], productOfTheOthers would return [24, 12, 8, 6]
# Function Name: productOfTheOthers
# Input: an array – for your submission use the test array [3, 9, 7, -2]
# Output: an array – when given the test array, your submission should return [-126, -42, -54, 189]
# Example: productOfTheOthers([3, 9, 7, -2]) => [-126, -42, -54, 189]
# Your array may have n integers, presume that n > 1.
# Would your function work if the input array contained zeroes?

# Solve the basic challenge, but this time do so without using division. Call this new function advProductOfTheOthers.
# Function Name: advProductOfTheOthers
# Input: an array – for your submission use the test array [0, 9, 7, 8, -2]
# Output: an array
# Example: advProductOfTheOthers([1,2,3,4]) => [24, 12, 8, 6]

def advProductOfTheOthers(num_array):
    product = 1 #start the variable to hold the product of all numbers except the number itself
    product_list = [] #final list to hold the values of each product
    for i in range(0,len(num_array)): #loop though num_array
        for n in num_array: #for each number in num_array
            #if n is different from the current number of number (i), then multiply it by product, else it is ignored
            if n != num_array[i]:
                product *= n 
        product_list.append(product) #add product to the product_list list
        product = 1  #restart the product variable
    return product_list

print('advProductOfTheOthers([3, 9, 7, -2]) =>', advProductOfTheOthers([3, 9, 7, -2]))
print('advProductOfTheOthers([1,2,3,4]) =>', advProductOfTheOthers([1,2,3,4]))