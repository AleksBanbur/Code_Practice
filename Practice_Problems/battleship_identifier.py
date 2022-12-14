#Problem
#Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.

#Class ID	Ship Class
#B or b	BattleShip
#C or c	Cruiser
#D or d	Destroyer
#F or f	Frigate
#Input
#The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains a character.

#Output
#For each test case, display the Ship Class depending on ID, in a new line.

#Constraints
#1 ≤ T ≤ 1000

t = int(input())
for i in range(t):
    letter = input()
    if letter == "B" or letter == "b" :
        print("BattleShip")
    elif letter == "C" or letter == "c" :
        print("Cruiser")
    elif letter == "D" or letter == "d" :
        print("Destroyer")
    elif letter == "F" or letter == "f" :
        print("Frigate")
