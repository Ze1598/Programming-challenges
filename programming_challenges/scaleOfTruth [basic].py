# Suppose you were given eight soccer balls), all of them seemingly identical. You are given a balance scale️ and told that one of the eight balls is slightly heavier than the others (outlierBall). What’s the fewest number of times you have to use the scale to find outlierBall? Write a function, scaleOfTruth, that will determine the minimum number of weighs that you’ll need to find outlierBall.
# Function Name: scaleOfTruth
# Input: None
# Output: an integer representing the minimum number of weighs needed to find outlierBall
# Seven of the footballs have an exactly even weight, only one of the footballs (outlierBall) has a greater weight.
# The balance scale is the only way that you can discern any physical difference between the eight footballs.
# The balance scale did not come with any reference weights – the only weights you have to use on the balance scale are the footballs themselves.

#my logic:
#start by picking the first half of the total number of balls (in this case we pick 4)
#then put them on each plate of the balance scale (so 25% of the total in each plate; 2 in this case)
#if the weight of both plates is the same then it means the outlierBall wasn't used in this test: discard/put asside the tested half (4) balls and now test the other half
#from testing the second half see which plate is heavier: take the balls in that plate and test them 
#repeat the process above until only 2 balls are being tested: this means there's only 1 ball in each plate, so we get an accurate answer of which one is the outlierBall
#in case there's an odd total of balls, we execute the process above, except in the beginning we pick the last ball (call it odd_ball) of the balls list and remove it from the list; if we can't find outlierBall from testing the rest of the balls then this means odd_ball is outlierBall


from random import choice

def scaleOfTruth():
#(1) Variable definition
    #this will be a list containing all the balls to be tested
    balls = [str(i) for i in range(1,9)]
    # balls = [str(i) for i in range(1,10)]
    #the outlierBall will be a randomly chosen ball from the balls list
    outlierBall = choice(balls)

#(1.1) If there's an odd number of balls, we pick the last ball of the bunch and call it odd_ball (no real meaning here) and remove it from the balls list; if after testing all the other balls we still can't find the outlierBall, then it means this odd_ball is the outlierBall
    if (len(balls)%2) != 0:
        odd_ball = balls[len(balls)-1]
        del balls[len(balls)-1]
    print('outlierBall:',outlierBall)
    #number of tests executed to find which ball is the outlierBall
    tries = 0
#(1.2) Pick the first half of balls which will be tested, and then divide this half in another half (so two quarters of the total) to put in each plate of the balance
    #this list will hold which balls are currently being tested
    being_tested = balls[0:(len(balls)//2)]
    print('being_tested:',being_tested)
    #the first plate will hold half of the balls in being_tested
    plate1 = being_tested[0:(len(being_tested)//2)]
    print('plate1:',plate1)
    #the second plate willd hold the other half of the ball in being_tested
    plate2 = being_tested[(len(being_tested)//2):]
    print('plate2:',plate2)
    
#(2) Weight distribution
    #if a plate isn't holding the outlierBall then its weight will be "normal" (interpreted as 1 here)
    #if it holds outlierBall then its weight is heavier (interpreted as 2)
    if outlierBall not in plate1:
        plate1_weight = 1 
    else:
        plate1_weight = 2
    if outlierBall not in plate2:
        plate2_weight = 1
    else:
        plate2_weight = 2
        
    # count= 0
    
#(3) Loop to execute the test until outlierBall is found    
    while True:
        '''print()'''
#(3.1) If there's only one ball in each plate, then the ball in the heavier plate is outlierBall
        if (len(plate1) == 1) and (len(plate2) == 1):
            print('len==1')
            tries += 1
            if plate1_weight > plate2_weight:
                print('The outlierBall is ball',plate1[0])
            else:
                print('The outlierBall is ball',plate2[0])
            break

#(3.2) If both plates have the same weight, outlierBall isn't in neither of the plates, then assign the other half of balls to being_tested, and then distribute being_tested between the plates; in the end reassign the weights according to the presence of outlierBall
        if plate1_weight == plate2_weight:
            tries += 1
            print('=')
            if balls[(len(balls)//2):] == (plate1 + plate2):
                print('The outlierBall is ball', odd_ball)
                break
            being_tested = balls[(len(balls)//2):]
            print('being_tested:',being_tested)
            plate1 = being_tested[0:(len(being_tested)//2)]
            print('plate1:',plate1)
            plate2 = being_tested[(len(being_tested)//2):]
            print('plate2:',plate2)
            if outlierBall not in plate1:
                plate1_weight = 1 
            else:
                plate1_weight = 2
            if outlierBall not in plate2:
                plate2_weight = 1
            else:
                plate2_weight = 2

#(3.3) If plate1 is heavier than plate2 then it means outlierBall is in plate1; being_tested is assigned just the balls in plate1; now distribute the new being_tested between the two plates (this means the plates were "resetted")
        elif plate1_weight > plate2_weight:
            tries += 1
            print('1>2')
            being_tested = plate1
            print('being_tested:',being_tested)
            plate1 = being_tested[0:(len(being_tested)//2)]
            print('plate1:',plate1)
            plate2 = being_tested[(len(being_tested)//2):]
            print('plate2:',plate2)
            if outlierBall not in plate1:
                plate1_weight = 1 
            else:
                plate1_weight = 2
            if outlierBall not in plate2:
                plate2_weight = 1
            else:
                plate2_weight = 2

#(3.4) If plate2 is heavier than plate1 then it means outlierBall is in plate2; being_tested is assigned just the balls in plate2; now distribute the new being_tested between the two plates (this means the plates were "resetted")
        else:
            tries += 1
            print('1<2')
            being_tested = plate2
            print('being_tested:',being_tested)
            plate1 = being_tested[0:(len(being_tested)//2)]
            print('plate1:',plate1)
            plate2 = being_tested[(len(being_tested)//2):]
            print('plate2:',plate2)
            if outlierBall not in plate1:
                plate1_weight = 1 
            else:
                plate1_weight = 2
            
            if outlierBall not in plate2:
                plate2_weight = 1
            else:
                plate2_weight = 2
        
        # count+=1 
        # if count==5:
        #     print('break')
        #     break
    return tries

print('scaleOfTruth(8) =>',scaleOfTruth())
# print('scaleOfTruth(9) =>',scaleOfTruth())