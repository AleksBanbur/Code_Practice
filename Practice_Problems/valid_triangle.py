#Problem
#Write a program to check whether a triangle is valid or not, when the three angles of the triangle are the inputs. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

#Input
#The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three angles A, B and C, of the triangle separated by space.

#Output
#For each test case, display 'YES' if the triangle is valid, and 'NO', if it is not, in a new line.

#Constraints
#1 ≤ T ≤ 1000
#1 ≤ A,B,C ≤ 180

t = int(input())
for i in range(t):
    (a,b,c) = map(int, input().split(" "))
    if a + b + c == 180 :
        print("YES")
    else :
        print("NO")
