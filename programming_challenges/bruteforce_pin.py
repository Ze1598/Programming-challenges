# https://www.codewars.com/kata/5263c6999e0f40dee200059d/solutions/python

'''
Bruteforce possible pin combinations
Make combinations taking into account each digit can be replaced by itself or any adjacent digit in a numpad like this:
1   2   3
4   5   6
7   8   9
    0
'''

def get_pins(observed):
    # The possible replace digits for each digit
    '''
    adjacent = [['0', '8'], 
                ['1', '2','4'], 
                ['2', '1', '3', '5'], 
                ['3', '2', '6'], 
                ['4', '1', '5', '7'], 
                ['5', '2', '4', '6', '8'], 
                ['6', '3', '5', '9'], 
                ['7', '4', '8'], 
                ['8', '0', '5', '7', '9'], 
                ['9', '6', '8'] 
                ]
    '''
    # A better way to store the adjacent digits
    adjacent = ['08', '124', '2135', '326', '4157', '52468', '6359', '748', '80579', '968']

    # List to contain the computed pins
    possibilities = []
    #Index of the observed digit being tested
    i = 0

    # First, loop through the observed number
    for digit in observed:
        # Then loop through the adjacent numbers to the current digit
        for num in adjacent[int(digit)]:
            # Then recursively find the pins for the input pin, with the left-most digit removed\
            # and loop through the returned pins
            for pin in get_pins(observed[i+1:]):
                pin_try = num + pin
                possibilities.append(pin_try)
            if num not in possibilities:
                possibilities.append(num)
        
        # Increment this variable to denote we moved to the next digit of the input pin
        i += 1
    
    # Return only the pins whose length is equal to the input pin's length
    return [pin for pin in possibilities if len(pin) == len(observed)]

# Input pin
print(sorted(get_pins('8')))
# Expected result
print(sorted(['5','7','8','9','0']))
print()
print(sorted(get_pins('11')))
print(sorted(["11", "22", "44", "12", "21", "14", "41", "24", "42"]))
print()
print(sorted(get_pins('369')))
print(sorted(["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]))


# Alternative solution (posted by BattleRattle)
'''
def get_pins(observed):
      map = [['8','0'], ['1','2','4'], ['1','2','3','5'], ['2','3','6'], ['1','4','5','7'], ['2','4','5','6','8'],
         ['3','5','6','9'], ['4','7','8'], ['5','7','8','9','0'], ['6','8','9']]
  return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] for y in get_pins(observed[1:])]
'''