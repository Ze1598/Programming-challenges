# https://discuss.codecademy.com/t/challenge-top-score-sorter/148011
# scoreSettler will take a list of unsorted scores plus the highest possible score and return a sorted list of all of the scores, in descending order from high score to low score.
# Function Name: scoreSettler
# Input: list of integers representing scores and a single integer for the highest possible score
# Output: A sorted list of integers in descending order
# Example: scoreSettler([ 1, 2, 3, 999999], 1000000) => [999999, 3, 2, 1]
# In your submission, please use as a test of your function the maximum value of 1218000, with a list of scores [874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600, 1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100]

def scoreSettler_easy(score_list, high_score):
    #simply sort and reverse the score_list and return it
    return sorted(score_list, reverse = True)
    
print('scoreSettler_easy([874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600, 1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100], 1218000) =>', scoreSettler_easy([874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600, 1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100], 1218000))
print()


def scoreSettler(score_list, high_score):
    #list to hold the sorted values
    sorted_score_list = []
    
    #while there's at least 1 value in score_list, determine which value is the highest (max_score), then append it to sorted_score_list, and remove it from score_list
    while score_list:
        max_score = 0 
        #initialize max_score
        for score in score_list: 
            #loop through score_list to determine max_score
            if score > max_score:
                max_score = score
        
        #if the current max_score is lower or equal to the highest score possible (high_score)
        if max_score <= high_score:
            sorted_score_list.append(max_score)
            #append max_score to sorted_score_list
            score_list.remove(max_score)
            #and then remove the current max_score from score_list
        else:
            #if the current max_score is higher than the highest score possible (high_score)
            score_list.remove(max_score)
            #just remove max_score from score_list

    return sorted_score_list
    
    
print('scoreSettler(scoreSettler([ 1, 2, 3, 999999], 1000000) =>', scoreSettler([ 1, 2, 3, 999999], 1000000))
print('scoreSettler([874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600, 1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100], 1218000) =>', scoreSettler([874300, 879200, 1172100, 1141800, 933900, 1177200, 1190200, 1110100, 1158400, 985600, 1047200, 1049100, 1138600, 1170500, 1064500, 1190000, 1050200, 1090400, 1062800, 1061700, 1218000, 1068000, 1127700, 1144800, 1195100], 1218000))