#Problem
#Shivam is the youngest programmer in the world, he is just 12 years old. Shivam is learning programming and today he is writing his first program.

#The task is very simple: given two integers A and B, write a program to add these two numbers and output it.

#Input Format
#The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains two Integers A and B.

#Output Format
#For each test case, add A and B and display the sum in a new line.

#Constraints
#1 ≤ T ≤ 1000
#0 ≤ A,B ≤ 10000

T = int(input())
for tc in range(T):
	# Read integers a and b.
	(a, b) = map(int, input().split(' '))
	
	ans = a + b
	print(ans)
