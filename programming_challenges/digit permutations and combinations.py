# https://discuss.codecademy.com/t/challenge-number-permutation/85775
# Create a program makeNumberBasic(z) which, when given an input of a number (z), returns the number of all possible permutations of digits (1 through 9 inclusive) that when added will equal z.


#Basic difficulty
def makeNumberBasic(z):
    possible_perms = [] #this will hold all the "correct" permutations (these include zeros)
    filt_perms = [] #this will hold all the permutations, not including zeros 
    filt = '' #this is just a simple string to be used as a means to extract the correct permutations without using zeros
    
    for i in range(1,100000): #permutations vary between 00001 (1) to 99999 inclusive
        if (sum(int(digit) for digit in str(i))) == z: #if the sum of i's digits == z then i is a "correct" permutation
            possible_perms.append(i) #i will then be added to the possible_perms list
    
    for item in possible_perms: #loop through each "correct" permutation in possible_perms
        for char in str(item): #loop through each digit of each "correct" permutation
            if int(char) != 0: #if that digit isn't zero then it is added to filt, a variable to hold just the current permutation 
                filt += char
        if int(filt) not in filt_perms: #if this current filt permutation isn't in the filt_perms list (a.k.a. the final permutations' list) then add filt to filt_perms
            filt_perms.append(int(filt))
            filt = '' #after that restart filt as an empty string
        else:
            filt = '' #even if that filt permutation was already in filt_perms, filt still needs to be restarted
    if len(filt_perms) == 0: #if there are no possible permutations
        print('There are no possible permutations of digits that when added will equal {}.'.format(z))
    else: #else
        print('There are {} possible permutations of digits that when added will equal {}.'.format(len(filt_perms),z))
        print('These are:',filt_perms)
   
#Intermediate difficulty
def makeNumber(z):
    possible_combs = [] #this will hold all the "correct" combinations (these include zeros)
    filt_combs = [] #this will hold all the combinations, not including zeros 
    final_combs = []
    filt = '' #this is just a simple string to be used as a means to extract the correct combinations without using zeros
    
    for i in range(1,100000): #combinations vary between 00001 (1) to 99999 inclusive
        if (sum(int(digit) for digit in str(i))) == z: #if the sum of i's digits == z then i is a "correct" permutation
            possible_combs.append(i) #i will then be added to the possible_combs list
    
    for item in possible_combs: #loop through each "correct" combination in possible_combs
        for char in str(item): #loop through each digit of each "correct" combination
            if int(char) != 0: #if that digit isn't zero then it is added to filt, a variable to hold just the current combination
                filt += char
        if (filt not in filt_combs) and (filt[::-1] not in filt_combs): #if this current filt combination isn't in the filt_combs list (a.k.a. the final combinations' list) then add filt to filt_combs
            filt_combs.append(filt)
            filt = '' #after that restart filt as an empty string
        else:
            filt = '' #even if that filt combination was already in filt_perms, filt still needs to be restarted
    for item in filt_combs: #loop through each of the filtered combinations to remove the ones with repeated digits
        for item2 in item:
            if item.count(item2) > 1:
                i = False #if a digit appears more than once in a combination make i False
            else:
                i = True #else i will be True
        if i == True: #if i is True then add the current combination to the final_combs list
            final_combs.append(int(item))
        else: #if i is False then just ignore this current combination
            pass
        
    if len(final_combs) == 0: #if there are no possible combinations
        print('There are no possible combinations of digits that when added will equal {}.'.format(z))
    else: #else
        print('There are {} possible combinations of digits that when added will equal {}.'.format(len(final_combs),z))
        print('These are:',final_combs)

makeNumberBasic(1)
print()
makeNumberBasic(2)
print()
makeNumberBasic(3)
print()
makeNumberBasic(43)
print()
makeNumberBasic(44)
print()
makeNumberBasic(45)
print()
print()
makeNumber(1)
print()
makeNumber(2)
print()
makeNumber(3)
print()
makeNumber(43)
print()
makeNumber(44)
print()
makeNumber(45)