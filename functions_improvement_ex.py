# functions improvement exercise
# times-table tester
import random

def intro():
    print("Times-table tester")
    print()
    
def question():
    testTable = int(input("Which times-table do you want to be tested on? "))
    return testTable


def output (UserAnswer, Ans):
    if UserAnswer == Ans:
        print('Well done, you got the correct answer!')
        print()
    else:
        print('Sorry, you got the answer wrong. The correct answer is'.format(Ans))
        print()

def calculations(Num1):
    Num2 = random.randrange(2,13)
    UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
    UserAnswer = int(UserAnswer)
    actualAnswer = Num1 * Num2
    return UserAnswer, actualAnswer
             
def number(testTable):
    Num1 = testTable
    return Num1

def program():
    intro()
    testTable = question()
    for questions in range(1,6):
        UserAnswer, actualAnswer = calculations(testTable)
        output(UserAnswer,actualAnswer)
        


    


# main progam
program()

