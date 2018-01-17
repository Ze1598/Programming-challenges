'''
You're building an ATM and want to know how many ways you can "break" a given amount of money into cash or change.
To do so, write a function, changeOptions, that when fed an amount of money n and a list of values S = { S1, S2, .. , Sm} (representing the possible coin or note denominations), will return the number of all the possible ways in which one can break down n into change.

Function Name: changeOptions
Input: n, an integer ≥0 and an integer array S which is the list of all denominations.
Output: an integer, the number of all of the possible combinations of coins and notes that add up to n
Example: changeOptions(5, [1, 2, 5, 10, .., 50000]) => 4
Where the amount is 5¢ (n=5) and the denominations are S = [1, 2, 5, 10, .., 50000], the possible combinations of coins and notes that add up to 5 are 1+1+1+1+1, 1+1+1+2, 1+2+2, 5, so your function would return 4.
The order of the coins and notes doesn't matter – 2¢+1¢+2¢ is the same amount of money as 2¢+2¢+1¢.
n and S both represent the number of cents – for example do not use €2.50 as an input, use 250 instead.
use as your sample problem n = 26730 and S = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
'''
#explanation of my logic:
#loop through the values in 'S', from the highest to the lowest
#if 'value' is lower or equal than 'n', subtract 'value' to 'n', and repeat this until 'n' = 0 
#after finishing the current change combination, repeat this process, starting at the second highest value from the previous sub list
#example using the sample problem: n = 26730, so the first value from 'S' to be used for the first combination would be 20000; then the second combination will start with the next value, in this case 10000, and so on, until only 1 is used (the lowest value in 'S'; this is the last combination possible)

def changeOptions(n, S):
    # '''debug
    combinations = [] #holds all the used change combinations
    current_comb = [] #this list holds the current combination, which is then appended to the 'combinations' list and resetted for the next combination
    sub_S = [] #a sub list of the orignal 'S' list; which will only hold the values relevant to the calculations
    n_ = n #create a copy of 'n', the original ammount of money; 'n_' will only be used during calculations
    sub_count = 0 #this variable is incremented each time a combination is finished (not counting the very first combination); it is used to decide the length of 'sub_S'
    comb_count = 0 #a counter for how many change combinations have been made; the value returned at the end of the function
    #loop through the values in 'S', from the highest to the lowest value (this means the list is reversed in the loop)
    for value in S[::-1]:
        #if 'value' is lower than 'n', then subtract 'value' from 'n' as many times as possible; this way the current 'value' will never have to be tested again
        if value <= n_: 
            #if 'sub_S' is still an empty list, then 'sub_S' is assigned as a sub list of 'S', containing only the relevant values to 'n'; will contain the highest value in 'S' that is lower or equal than 'n', and all the other values lower than that
            if sub_S == []:
                highest = S.index(value) #this variable is later used to automatize the creation of the other 'sub_S'
                sub_S = S[:highest][::-1]
            subtract = int(n_/value)
            n_ -= subtract * value
            # '''debug
            # for i in range(subtract):
            current_comb.append('{} * {}'.format(value,subtract))
    # '''debug
    # print('current_comb',current_comb)
    combinations.append(current_comb)
    current_comb = []
    n_ = n #reset 'n_' to the value of the initial 'n'
    comb_count += 1 #one combination has been created, so increment 'comb_count' by one
    '''debug
    # print('sub_S',sub_S)
    # print()
    # print()'''
    
    #now to get the rest of the combinations, use the sub list 'sub_S'
    #to make the process of creating the following sub lists automatic, the 'sub_count' variable comes into play: 
    #each time a new sub list is created, its highest value will be the second highest value from the previous sub list, and so on, until 'sub_S' is empty ('highest - sub_count < 0')
    while (highest - sub_count) > 0:
        for value in sub_S:
            if value <= n_: #if value is lower than n, then subtract value from n as many times as possible, this way the current value will never have to be tested again
                subtract = int(n_/value)
                n_ -= subtract * value
                # '''debug 
                # for i in range(subtract):
                current_comb.append('{} * {}'.format(value,subtract))
        
        # print('current_comb',current_comb)
        combinations.append(current_comb)
        current_comb = []
        #reset and increment the necessary variables
        n_ = n
        sub_count += 1
        sub_S = S[:(highest - sub_count)][::-1] #this is used to create the new sublist
        comb_count += 1
        '''debug
        # print('sub_S', sub_S)
        # print()'''
        
    # return len(combinations)
    # return comb_count
    # return combinations
    for item in combinations:
        print(item)
    return len(combinations)

print('changeOptions(5, [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]) =>', changeOptions(5, [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]))
print()
print('changeOptions(26730, [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]) =>', changeOptions(26730, [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]))