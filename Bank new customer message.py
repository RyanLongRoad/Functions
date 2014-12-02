#Ryan Cox
#02/12/14
#Bank program

def information():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")
    gender = input("Please enter your gender: ")
    house = input("Please enter your house number/name: ")
    street = input("Please enter your street name: ")
    town = input("Please enter your town name: ")
    postcode = input("Please enter your postcode: ")
    return firstName, lastName, gender

def titleconverter(gender):
    if gender == "male":
        title = "Mr"
    elif gender == "female":
        title = "Ms"
    return title
  
    

def message(title, firstName, lastName):
    print("Welcome {0} {1} {2} to Long Road Bank.".format(title, firstName, lastName))

    
def engine():
    firstName, lastName, gender = information()
    title = titleconverter(gender)
    message(title, firstName, lastName)

#Main Program
engine()

