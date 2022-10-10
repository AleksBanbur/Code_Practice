#Problem
#If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.

#Input
#The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains an integer N.

#Output
#For each test case, display the sum of first and last digits of N in a new line.

#Constraints
#1 ≤ T ≤ 1000
#1 ≤ N ≤ 1000000

for i in range(int(input())):
    s = input()
    print(int(s[0]) + int(s[len(s) - 1]))
