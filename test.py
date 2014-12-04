#Ryan Cox
#04/12/14
#Last one loses

import random


def number_of_counters():
    n = random.randint(1, 21)

    print(n)
    return n

def play(n):
    
    while n >=0:
        number = int(input("please enter the number you wish to subtract (1, 2 or 3): "))
        if number == 1:
            number = n - number
    print (number)

def engine():
    n = number_of_counters()
    play(n)
    


