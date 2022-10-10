#Problem
#Given a list of T integers, for each of them calculate the number of occurrences of the digit 4 in the decimal representation.

#Input
#The first line of input consists of a single integer T, denoting the number of integers in the list.

#Then, there are T lines, each of them contain a single integer from the list.

#Output
#Output T lines. Each of these lines should contain the number of occurences of the digit 4 in the respective integer from the list.

#Constraints
#1 ≤ T ≤ 105
#(Subtask 1): 0 ≤ Numbers from the list ≤ 9 - 33 points.
#(Subtask 2): 0 ≤ Numbers from the list ≤ 109 - 67 points.

t = int(input())
for i in range(t):
    fours = 0
    num = int(input())
    while(num):
        if(num%10 == 4):
            fours +=1
        num = int(num/10)
    print(fours)
