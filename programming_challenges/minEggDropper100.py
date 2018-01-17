# Suppose that you had 100 eggs in a 100-floor skyscraper, and you wanted to conduct an experiment to find out the highest floor (criticalFloor) from which you could drop an egg without breaking it… but you’re also really hungry so you don’t want to waste any eggs.

# Write a function, minEggDropper100, that will determine the minimum number of egg drops (minDrops100) you’d need to find the criticalFloor.

# Function Name: minEggDropper100
# Output: minDrops100 – an integer representing the minimum number of drops needed to find the criticalFloor
# An egg that survives a fall can be used again.
# A broken egg must be discarded.
# The eggs are all incredibly similar – the effect of a fall from a particular floor is the same for all eggs.
# If an egg survives a fall from floor n, then it would also survive a fall from the floors below it: floor n-1, floor n-2, etc.
# If an egg does not survive a fall from floor n, then it would also not survive a fall from the floors above it: floor n+1, floor n+2, etc.
# You should not presume that an egg would survive a fall from the first floor, nor should you presume that it would not survive a fall from the 100th floor!
from random import randint

def minEggDropper100():
    
#(1) Variables definition
    #[first, last] floors of the skyscraper
    skyscraper = [1, 100] 
    #number of eggs available to test
    eggs_available = 100 
    #minimum number of egg drops to find criticalFloor
    minDrops100 = 0
    #so the program doesn't always return the same result, let's generate a different criticalFloor for each time the function is executed: criticalFloor can be any floor from the skyscraper (in this case between floor 1 and 100,inclusive)
    gen_criticalFloor = randint(1,100)
    #the range of the testing; starts between the first and last floor, inclusive
    test_low_high = [skyscraper[0], skyscraper[1]]
    #initiate criticalFloor as 0 just to define the variable
    criticalFloor = 0
    
    '''print('criticalFloor:', gen_criticalFloor)'''
    
#(2) Loop to test if an egg breaks when dropped from a certain floor; the condition here doesn't matter since the loop will be terminated via the break statement
    while True:
#(2.1) If there are no more eggs available
        if eggs_available == 0:
            print('There are no more eggs available to test.')
            break
        
#(2.2) If the test range is just between two floors (test range is 1) then test one last time to see which one of them is the criticalFloor
        if (test_low_high[1] - test_low_high[0]) == 1:
            minDrops100 += 1
            if test_low_high[1] > gen_criticalFloor:
                criticalFloor = test_low_high[0]
                break
            else:
                criticalFloor = test_low_high[1]
                break
        
#(2.2) If the test range is between more than 2 floors (test range > 1)
        else:
            #the test floor is the middle floor of test_low_high
            test_floor = (test_low_high[0] + test_low_high[1]) // 2
            #if we are gonna drop another egg, then increment minDrops100 (the number of drops) by 1
            minDrops100 += 1
            
#(2.2.1) Egg breaks
            if test_floor >= gen_criticalFloor:
                #if the egg breaks we now have one less egg to test
                eggs_available -= 1
                #delimit the test range: it is now between the already assigned floor in the variable, test_low_high[0], and the current test_floor
                test_low_high[1] = test_floor
            
#(2.2.2) Egg doesn't break
            else:
                #delimit the test range: it is now between the current test_floor and the floor already assigned in the variable, test_low_high[1]
                test_low_high[0] = test_floor
        
        '''print(minDrops100, 'l_h:', test_low_high, 'range:', test_low_high[1] - test_low_high[0], 'floor:',test_floor, 'crit:', gen_criticalFloor)   '''     
    
#(3) End the script by outputting some information, and returning the initial objective: minDrops100
    print('Eggs left: ', eggs_available)
    print('criticalFloor: ', criticalFloor)
    return minDrops100 - 1

print('minEggDropper100() =>',minEggDropper100())