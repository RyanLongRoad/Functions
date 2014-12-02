#Ryan Cox
#02/12/14
#A program that asks the user to enter an odd number, validates that the number is odd and then prints an inverted pyramid of stars based on that number
#isn't alligning correctly

def checkodd():
    number = 2
    while number % 2 == 0:
        number = int(input("please enter an odd number: "))
    return number
    
  
def stars(number):
    while number >= 1:
            print("{: ^5}".format('*' * number ))
            number = number - 2
            
    return number
        

def engine():
    number = checkodd()
    
    stars(number)
    

#Main program
engine()
