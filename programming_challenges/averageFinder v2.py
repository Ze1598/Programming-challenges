'''#https://discuss.codecademy.com/t/challenge-calculate-max-min-and-averages/214283
#Write a function, averageFinder that will return the mean and mode of your race times.
#Function name: averageFinder
#Input: an array with race times, each a natural number representing the minutes it took you to finish your run (you can presume that race times are rounded up to the nearest minute so we do not have to deal with seconds)
#Output: an array, with mean time and mode time (in that order)
#Example: averageFinder([500, 450, 400, 400, 375, 350, 325, 300]) => [387.5, 400]'''

def averageFinder(times_array):
    #list to be returned at the end, containing, in this order: Mean, Mode,
    results = []
    #sum of all the items in 'times_array'
    times_sum = 0
    #number of items in 'times_array'
    number_items = 0
    #sorted version of 'times_array'
    sorted_arr = []
    #value to be used as condition to find the minimum value in 'times_array'
    min_value = float('inf')
    #loop through 'times_array', each time find the minimum value in it, append it to 'sorted_arr' and then remove it from 'times_array'; repeat until 'times_array' is empty
    while times_array:
        for i in times_array:
            if i < min_value:
                min_value = i
        times_array.remove(min_value)
        sorted_arr.append(min_value)
        min_value = float('inf')
    
    #loop through 'sorted_arr' to get the values needed for the Mean, then append the Mean to 'results'
    for item in sorted_arr:
        times_sum += item
        number_items += 1
    
    results.append(times_sum/number_items)

    print(sorted_arr)
    print('times_sum:', times_sum,'number_items:',number_items)
    
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
    Mode = 0
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
            Mode = i
        #reset counter_current
        counter_current = 1
        #increment 'index' by 1 because the loop is moving to the next index of the list
        index += 1
    print(Mode, 'frequency:', counter_max)
    results.append(Mode)
    return results

print('averageFinder([500, 450, 400, 400, 375, 350, 325, 300]) =>', averageFinder([500, 450, 400, 400, 375, 350, 325, 300]))