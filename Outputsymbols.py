#Ryan Cox
#02/12/14
#Takes an integer n and a character symbol and displays it on the same line, the symbol n times.

import sys

def information():
    n = int(input("Please enter the number of repeats: "))
    character = input("please enter the character: ")
    return character, n

def loop(character, n):
    for loops in range(n):
        print(character, end="") 

def engine():
    character, n = information()
    loop(character, n)

#Main Program

engine()
