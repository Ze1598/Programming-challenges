'''#https://discuss.codecademy.com/t/challenge-calculate-max-min-and-averages/214283
#Write a function, averageFinder that will return the mean and mode of your race times.
#Function name: averageFinder
#Input: an array with race times, each a natural number representing the minutes it took you to finish your run (you can presume that race times are rounded up to the nearest minute so we do not have to deal with seconds)
#Output: an array, with mean time and mode time (in that order)
#Example: averageFinder([500, 450, 400, 400, 375, 350, 325, 300]) => [387.5, 400]'''

#logic behind the program
#start with the mean: sum all the items in the input array and then divide it by the number of items the array contains
#for the mode, simply loop through the input array, and see how many times each item appears, then one that appears the most then is the mode
#before returning the 'results', append the mean and the mode to it

def averageFinder(times_array):
    #this list will contain the mean and mode obtained
    results = []
    #variable to hold the sum of all the times in 'times_array'
    times_sum = 0 
    #variable to count how many items 'times_array' contains
    times_count = 0
    #this variable will the mode that will be returned in the end
    mode = 0
    #counter for the most frequen item in 'times_array'
    mode_counter = 0
    #counter to be used inside the loop in each instance
    mode_counter2 = 0
    #loop through 'times_array' to calculate the mean
    for i in times_array:
        times_sum += i
        times_count += 1
    results.append(times_sum/times_count)
    #loop through 'times_array' to find the mode
    for i in times_array:
        for i2 in times_array:
            #if we find another instance of the current item then increment its counter by 1
            if i2 == i:
                #a condition to be executed only the very first time the loop is started(both the nested and outer loops)
                if (i == times_array[0]) and (mode_counter == 0):
                    mode = i
                    mode_counter += 1
                #in al the other instances simply increment 'mode_counter2' by 1
                else:
                    mode_counter2 += 1
        #if 'mode_counter2' is higher than 'mode_counter' which holds the most frequent item so far, then the mode becomes the item being currently tested, and 'mode_counter' now holds the value of the current 'mode_counter2'
        if mode_counter2 > mode_counter:
            mode = i
            mode_counter = mode_counter2
        #before finishing this instance of the loop reset 'mode_counter2'
        mode_counter2 = 0
        
    results.append(mode)
    print('times_sum:', times_sum, 'times_count:',times_count)
    return results
    
print('averageFinder([500, 450, 400, 400, 375, 350, 325, 300]) =>', averageFinder([500, 450, 400, 400, 375, 350, 325, 300]))