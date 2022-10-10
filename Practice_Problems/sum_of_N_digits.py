#Problem
#You're given an integer N. Write a program to calculate the sum of all the digits of N.

#Input
#The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.

#Output
#For each test case, calculate the sum of digits of N, and display it in a new line.

#Constraints
#1 ≤ T ≤ 1000
#1 ≤ N ≤ 1000000

T=int(input())
for i in range(T):
    num=int(input())
    sum=0
    for j in str(num):
        sum+=int(j)
    print(sum)
