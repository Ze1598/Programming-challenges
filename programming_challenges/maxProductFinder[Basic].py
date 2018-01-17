# https://discuss.codecademy.com/t/challenge-max-product-finder/113074
# Given an array of integers, write a function, maxProductFinder, that finds the largest product that can be obtained from any 3 integers in the array.

def maxProductFinder(int_array):
    #start by finding the 3 smallest numbers and 3 biggest numbers in int_array
    #to get the numbers i based myself off this code: http://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-28.php#h_one
    min1 = min2 = min3 = float('inf') #assign  min1, min2 and min3 to the value of positive infinity; these will be the 3 smallest numbers in int_array
    max1 = max2 = max3 = float('-inf') #assign max1, max2 and max3 to the value of negstive infinity; these will be the 3 biggest numbers in int_array
    
    for num in int_array: #loop through int_array
        if num > max3:
            if num > max2: #if num > max2, max3 (if num is bigger than negative infinity in the first loop)
                if num >= max1: #if num is also bigger or equal than max1 
                    max1, max2, max3 = num, max1, max2 #then max1 will be num; max2 will be the value of max1 and max3 the value of max2
                else: #(num > max2,max3) and (num < max1)
                    max2 = num
            else: #(num > max3) and (num <= max2)
                max3 = num
    # print('max1-',max1,'max2-',max2,'max3-',max3)
    
    for num in int_array:
         if num < min3: 
            if num < min2: #if num < min2, min3 (if num is smaller than positive infinity in the first loop)
                if num <= min1: #if num is also smaller or equal than min1
                    min1, min2, min3 = num, min1, min2 #then min1 will be num; min2 will be the value of min1 and min3 the value of min2          
                else: #(num < max2,max3) and (num > max1)
                    min2 = num
            else: #(num < max3) and (num >= max2)
                min3 = num
    # print('min1-',min1,'min2-',min2,'min3-',min3)

    #now that i have all 6 important numbers: 3 smallest and 3 biggest, i check which product is the wanted result
    #first we have product of min1*min2 and max1*max2; then we multiply of these two products by: the smallest and biggest numbers, 3rd smallest and 3rd biggest numbers
    return max(min1*min2*min3,max1*max2*max3,min1*min2*max1,max1*max2*min1)

    
    
print('maxProductFinder([-8, 6, -7, 3, 2, 1, -9]) =>',maxProductFinder([-8, 6, -7, 3, 2, 1, -9]))
print('maxProductFinder([-6, -8, 4, 2, 5, 3, -1, 9, 10]) =>',maxProductFinder([-6, -8, 4, 2, 5, 3, -1, 9, 10]))
print('maxProductFinder([6, 8, 4, 2, 5, 3, 1, 9, 10]) =>',maxProductFinder([6, 8, 4, 2, 5, 3, 1, 9, 10]))