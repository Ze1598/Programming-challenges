# https://discuss.codecademy.com/t/challenge-find-the-missing-number/221144
# You have a bag containing tiles with numbers [1, 2, 3, …, 100] written on them. Each number appears exactly once, so there are 100 tiles and 100 numbers. Now, without looking, one number tile is randomly picked out of the bag and discarded. Write a function, missingNo, that will find the missing number.
# Function Name: missingNO
# Input: an array, [1, 2, …, 100] with one number between 1 and 100 missing.
# Output: an integer, the “missing” number in the array
# Example: missingNo([1, 3, …, 100]) => 2 if the array was missing the number 2. Please include in your submission a test array with number 66 missing.
# The array may not be sorted.
# The removal of a number from the bag is totally random, there is no way to tell what number it was by the process of removing it (e.g. you cannot feel what number is written on the tile)
# You may look in the bag of number tiles and interact with the contents once the random number is removed. So, you can lay all of the tiles out,
from random import shuffle, choice, randint

def missingNO(arr):
#Loop through 'arr' by testing each number 'n': if 'n+1' is lower than the highest value in 'arr' and it is not in 'arr', and 'n-1' is higher than the lowest value in 'arr' and it is not in 'arr', then 
    for n in arr:
        if (n+1< max(arr)) and (n-1> min(arr)):
            return n + 1
        elif ((n+1 not in arr) or (n-1 not in arr)):
            return n - 1


# You replace the missing number in the bag, so you again have 100 tiles numbered from 1 to 100. This time, you remove two random number tiles. Write a function, missingNOs, that will find the missing numbers.
# Function Name: missingNOs
# Input: an array, [1, 2, …, 100] with two numbers between 1 and 100 missing.
# Output: an array of two integers, showing both “missing” numbers in the array in any order
# Example: missingNOs([1,4, …, 100) => [2, 3]

def missingNOs(arr):
    #list to contain the two numbers missing from 'arr'
    missing = []
#Loop through 'arr' by testing each number 'n'
    for n in arr:
#if 'n+1' is lower than the highest value in 'arr', and 'n+1' is not in 'arr':
        if (n + 1 < max(arr)) and ((n + 1) not in arr):
#and if 'n+1' is not in 'missing' already then append 'n+1' to 'missing'
            if ((n + 1) not in missing):
                missing.append(n + 1)
#if 'n+1' is higher than the lowest value in 'arr', and 'n-1' is not in 'arr':
        elif (n - 1 > min(arr)) and ((n - 1) not in arr):
#and if 'n-1' is not in 'missing' already then append 'n-1' to 'missing'
            if ((n - 1) not in missing):
                missing.append(n - 1)
    return missing

# Write a function, missingNoKetsuban, that will efficiently solve for a bag of size n (array elements in range from 1 to n) exactly k numbers missing from the bag.
def missingNoKetsuban(arr):
    #list to contain the two numbers missing from 'arr'
    missing = []
#Loop through 'arr' by testing each number 'n': if 'n+1' or 'n-1' is not in the list then it is a missing number; append 'n+1' or 'n-1' to the 'missing' list
#repeat the loop while 'missing'\'s length is smaller than 100 - the lenght of 'arr'
    while len(missing) < 100-len(arr):
        for n in arr:
#if 'n+1' is lower than the highest value in 'arr', and 'n+1' is not in 'arr':
            if (n + 1 < max(arr)) and ((n + 1) not in arr):
#and if 'n+1' is not in 'missing' already then append 'n+1' to 'missing'
                if ((n + 1) not in missing):
                    missing.append(n + 1)
#if 'n+1' is higher than the lowest value in 'arr', and 'n-1' is not in 'arr':
            elif (n - 1 > min(arr)) and ((n - 1) not in arr):
#and if 'n-1' is not in 'missing' already then append 'n-1' to 'missing'
                if ((n - 1) not in missing):
                    missing.append(n - 1)
    return missing


#these examples are missing one specific number: 66 and 2, respectively
a = list(range(1,101))
a.remove(66)
b = list(range(1,101))
b.remove(2)
c = list(range(1,101))
c.remove(choice(c))
shuffle(a)
shuffle(b)
shuffle(c)
'''
print('missingNO([1, ..., 65, 66, ..., 100]) =>',missingNO(a))
print()
print('missingNO([1, 3, ..., 100]) =>',missingNO(b))
print()
print('missingNO([1, ..., 100]) =>',missingNO(c))
print()
'''

#these examples are missing two numbers: the first example is missing two random numbers, the second example is missing 2 and 3
d = list(range(1,101))
d.remove(choice(d))
d.remove(choice(d))
e = list(range(1,101))
e.remove(2)
e.remove(3)
shuffle(d)
shuffle(e)
'''
print('missingNOs([1, …, 100]) =>',missingNOs(d))
print()
print('missingNOs([1, …, 100]) =>',missingNOs(e))
print()
'''

#for this last example i estabelished that this array will be missing between one and five missing numbers
f = list(range(1,101))
for i in range(randint(1,5)):
    f.remove(choice(f))
shuffle(f)
'''
print('missingNoKetsuban([1, …, 100]), missing {} =>'.format(100-len(e)),missingNoKetsuban(f))
'''

print('missingNoKetsuban([1, …, 100])=>',missingNoKetsuban(a))
print('missingNoKetsuban([1, …, 100])=>',missingNoKetsuban(b))
print('missingNoKetsuban([1, …, 100])=>',missingNoKetsuban(c))
print('missingNoKetsuban([1, …, 100])=>',missingNoKetsuban(d))
print('missingNoKetsuban([1, …, 100])=>',missingNoKetsuban(e))
print('missingNoKetsuban([1, …, 100])=>',missingNoKetsuban(f))