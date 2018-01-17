# Write a function, getMedian, that will return the median value of a list of numbers.
# Function Name: getMedian
# Input: An unsorted List of integers
# Output: The integer which is the median value of the input list.
# Examples: getMedian([6,10,2,5,9,3,10,12,18,-3]) => 7.5 (average of the middle two values)
# getMedian([5,10,-3,7,9]) => 7
def getMedian(num_list):
    #the following chunk of code is used to sort the num_list in ascending order, the result is sorted_num_list; this is equivalent to sorted(num_list)
    sorted_num_list = []
    while num_list:
        min_num = float('+inf')
        for num in num_list:
            if num < min_num:
                min_num = num
        sorted_num_list.append(min_num)
        num_list.remove(min_num)
    
    #test if the number of items in sorted_num_list is even or odd
    if len(sorted_num_list)%2 == 0:
        #if it's even the median will be the average of the two middle numbers in sorted_num_list
        median_value = (sorted_num_list[len(sorted_num_list)//2] + sorted_num_list[(len(sorted_num_list)//2) - 1]) / 2
    else:
        #if it's odd then the madian will just be the middle number of sorted_num_list
        median_value = sorted_num_list[len(sorted_num_list)//2]
    
    return median_value
        
print('getMedian([6,10,2,5,9,3,10,12,18,-3]) =>', getMedian([6,10,2,5,9,3,10,12,18,-3]))
print('getMedian([5,10,-3,7,9]) =>', getMedian([5,10,-3,7,9]))