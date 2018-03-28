#https://www.hackerrank.com/challenges/a-very-big-sum/problem
'''You are given an array of integers of size N. You need to 
print the sum of the elements in the array, keeping in mind 
that some of those integers may be quite large. '''

def aVeryBigSum(n, ar):
    return sum(int(x) for x in str(ar).split())

n = 5
ar = '1000000001 1000000002 1000000003 1000000004 1000000005'
#n = int(input().strip())
#ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
if result == 5000000015:
    print(f'aVeryBigSum({n},{ar}) => {result}')
    
'''------------------------------------------------------------'''

#https://www.hackerrank.com/challenges/diagonal-difference/problem
'''Given a square matrix of size N*N, calculate the absolute 
difference between the sums of its diagonals.'''

def diagonalDifference(a):
    sum_left = 0
    sum_right = 0
    #To get the left diagonal sum, sum its numbers starting at the top-left number
    for i in range(len(a)):
        sum_left += a[i][i]
    j = 0
    #To get right diagonal sum, sum its numbers starting at the top-right number
    for i in range(len(a)-1, -1, -1):
        sum_right += a[j][i]
        j += 1
    return abs(sum_left - sum_right)

n = 3
a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
#a = []
#for a_i in range(n):
   #a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   #a.append(a_t)
result = diagonalDifference(a)
if result == 15:
    print(f'diagonalDifference({a}) => {result}')

'''------------------------------------------------------------'''

#https://www.hackerrank.com/challenges/compare-the-triplets/problem
'''Alice and Bob each created one problem for HackerRank. A reviewer 
rates the two challenges, awarding points on a scale from 1 to 100 for 
three categories: problem clarity, originality, and difficulty.
We define the rating for Alice's challenge to be the triplet A(a0, a1, a2),
and the rating for Bob's challenge to be the triplet B(b1, b2, b3).
1 point is awarded per category; if a category results in a tie, nobody
wins the point.
Given A and B, can you compare the two challenges and print their 
respective comparison points?'''

def solve_reviews(a0, a1, a2, b0, b1, b2):
    alice_points = 0
    bob_points = 0
    #Simply compare each category; ties are ignored since no one gets points for it
    if a0 > b0: alice_points += 1
    elif a0 < b0: bob_points += 1
    if a1 > b1: alice_points += 1
    elif a1 < b1: bob_points += 1
    if a2 > b2: alice_points += 1
    elif a2 < b2: bob_points += 1
    return alice_points, bob_points

# a0, a1, a2 = input().strip().split(' ')
# a0, a1, a2 = [int(a0), int(a1), int(a2)]
# b0, b1, b2 = input().strip().split(' ')
# b0, b1, b2 = [int(b0), int(b1), int(b2)]
a0, a1, a2 = 5, 6, 7
b0, b1, b2 = 3, 6, 10
result = solve_reviews(a0, a1, a2, b0, b1, b2)
if result == (1,1):
    print(f'solve({a0, a1, a2, b0, b1, b2}) => {result}')

'''------------------------------------------------------------'''

#https://www.hackerrank.com/challenges/grading/problem
'''HackerLand University has the following grading policy: Every student 
receives a grade in the inclusive range from 1 to 100; Any grade less 
than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's 
grades according to these rules: If the difference between the grade and 
the next multiple of 5 is less than 3, round grade up to the next multiple of 5;
If the value of grade is less than 38, no rounding occurs as the result 
will still be a failing grade.
Given the initial value of grade for each of Sam's n students, write code to 
automate the rounding process.'''

def solve_grades(grades):
    #Loop through the 'grades'
    for grade in grades:
        #The conditionals test if the next number or the one after that is a multiple
        #of 5: if it is then "round" the grade to that multiple
        #And of course, the original grade needs to be at least 38
        if grade > 37 and ((grade+1)%5) == 0:
            grades[grades.index(grade)] = grade + 1
        elif grade > 37 and ((grade+2)%5) == 0:
            grades[grades.index(grade)] = grade + 2
    return grades

# n = int(input().strip())
# grades = []
# grades_i = 0
# for grades_i in range(n):
#    grades_t = int(input().strip())
#    grades.append(grades_t)
n = 4
grades = [73, 67, 38, 33]
result = solve_grades(grades)
if result == [75, 67, 40, 33]:
    print(f'solve_grades(grades) => {result}')
