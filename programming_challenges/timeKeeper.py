'''# https://discuss.codecademy.com/t/challenge-calculate-max-min-and-averages/214283
# Write a function, timeKeeper that will help you out. timeKeeper will take an input, n a positive integer representing the number of minutes it took you to complete your latest run, and then return an array of the following vital statistics about all of your runs to date:

# the longest time you’ve taken to date (maxTime)
# the shortest (best) time you’ve taken to date (minTime)
# the mean of all of your race times (meanTime)
# the mode of all of your race times (modeTime)
# the median1 of all of your race times (medianTime)
# Function name: timeKeeper
# Input: a race time n, a natural number in minutes (you can presume that race times are rounded up to the nearest minute so we do not have to deal with seconds). Each time you insert a new time, n, it is added to an array that contains all of your historical race times.
# Output: an array, with longest time, shortest time, mean time, and mode time (in that order)
# Example: with an existing array of [500, 450, 400, 400, 375, 350, 325, 300] for your historical times and your new time of 320 to insert, timeKeeper(320) => [500, 300, 380, 400, 375]'''
#my modification to the challenge is that the function receives to inputs: 'times_array' which is an array of times, and 'n', which is the the original input from the challenge

#logic behind the program:
#append 'n' to 'times_array' and then sort it in ascending order, which results in 'sorted_arr'
#loop through the sorted list to get the values needed to calculate the mean, which includes the length of the list
#to get the mode loop through the sorted list and see which number has most consecutive appearances (since it is sorted, to see how many times a number is in the list we can simply see how many times in a row it appears)
#to get median test if the list has an odd or even lenght: if odd then the median is simply the middle value in the list; if it's even, the median is the average of the two values in the middle
#the max value is the last item of the list
#the min value is the first item of the list
#now that all the values were found, append them in the desired order to 'results' and return it


def timeKeeper(times_array,n):
    times_array.append(n)
    #list to be returned at the end, containing, in this order: maxTime, minTime, meanTime, modeTime, medianTime
    results = []
    #sum of all the items in 'times_array'
    times_sum = 0
    #number of items in 'times_array'
    arr_len = 0
    #sorted version of 'times_array' in ascending order
    sorted_arr = []
    #value to be used as condition to find the minimum value in 'times_array'
    min_value = float('inf')

#Sort the array    
    #loop through 'times_array', each time find the minimum value in it, append it to 'sorted_arr' and then remove it from 'times_array'; repeat until 'times_array' is empty
    while times_array:
        for i in times_array:
            if i < min_value:
                min_value = i
        times_array.remove(min_value)
        sorted_arr.append(min_value)
        min_value = float('inf')

#Get the array length and the values needed to calculate the Mean    
    #loop through 'sorted_arr' to get the values needed for the Mean, then append the Mean to 'results'
    for item in sorted_arr:
        times_sum += item
        arr_len += 1
    

    print('sorted_arr:',sorted_arr)
    print('times_sum:', times_sum,'number_items:', arr_len)
    
#Get the Mode    
    #now to find the Mode
    #simply the index of the current value relative to 'sorted_arr'
    index = 0
    #number to be added to the index, so we can look into the following items in 'sorted_arr'
    n = 1
    #the next two counter variables start at 1 so when counting how many times an item appears in 'sorted_arr' it counts the its first appearance 
    #maximum frequency of an item found in 'sorted_arr'
    counter_max = 1
    #how many times the current item is present in 'sorted_arr'
    counter_current = 1
    #the value that appears the most in 'sorted_arr'
    modeTime = 0
    #now to find the mode (modeTime)
    #loop through 'sorted_arr'; because this list is sorted, in order to find which item has the highest number of instances in the list we simply test how many times in a row that number appears
    for i in sorted_arr:
        #while the following indexes contain the same number has the one being currently tested, increment 'counter_current' each time the condition the following number is the same as the current one
        while ((index + n) <= (len(sorted_arr) - 1)) and (i == sorted_arr[index+n]):
            counter_current += 1
            n += 1 
        #after the condition returns False reset 'n' to 1
        n = 1
        #if the current number has more instances in 'sorted_arr' than the previous highest, this current number becomes the number to have the most instances
        if counter_current > counter_max:
            counter_max = counter_current
            modeTime = i
        #reset counter_current
        counter_current = 1
        #increment 'index' by 1 because the loop is moving to the next index of the list
        index += 1
    print('Mode:',modeTime, 'frequency:', counter_max)

#Get the Median
    #now to find the Median
    #if 'sorted_arr' has an odd length then the Median is the middle value
    #if 'sorted_arr' has an even length then the Median is the average of the two middle values
    if (arr_len%2) == 0:
        medianTime = (sorted_arr[arr_len//2] + sorted_arr[(arr_len//2) + 1]) / 2
    else:
        medianTime = sorted_arr[arr_len//2]

#Finally append the values wanted to 'results': maxTime, minTime, meanTime, modeTime and medianTime    
    #since 'sorted_arr' is sorted in ascending order, the highest time will simply be the last time of the list
    maxTime = sorted_arr[arr_len-1]
    results.append(maxTime)
    
    #since 'sorted_arr' is sorted in ascending order, the lowest time will simply be the first time of the list
    minTime = sorted_arr[0]
    results.append(minTime)
    
    #the mean(meanTime) is the result of sum of all items in 'sorted_arr' (times_sum divided by the len of 'sorted_arr' (arr_len)
    meanTime = times_sum/arr_len
    results.append(meanTime)
    
    #append to 'results' the previously found modeTime
    results.append(modeTime)
    
    #append to 'results' the previously found medianTime
    results.append(medianTime)
    
    return results

test_array = [500, 450, 400, 400, 375, 350, 325, 300]
print('timeKeeper(320) =>', timeKeeper(test_array,320))