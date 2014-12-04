#Ryan Cox
#04/12/2014
#a program to convert measurements between feet and inches and metres and centimetres.

def decision():
    choice = input("Please enter the units you have('feet and inches' OR 'metres and cenimetres') ")

    if choice == "feet and inches":
        imperial_to_metric()
        
        
    elif choice == "metres and cenimetres":
        metric_to_imperial()

    


def imperial_to_metric():
    feet = int(input("enter the number of feet you wish to convert: "))
    inches = int(input("enter the number of inches you wish to convert: "))

    total = feet * 12
    total = total + inches

    cm = total/0.397
    m = cm // 100
    cm = cm % 100

    print("{0} feet and {1} inches is equal to {2} metres and {3} centimetres".format(feet, inches, m, cm))
    
    
    
    


def metric_to_imperial():
    m = int(input("enter the number of metres you wish to convert: "))
    cm = int(input("enter the number of centimetres you wish to convert: "))

    total = m * 100
    total = total + cm
    
    inches = total * 0.397
    feet = inches // 12
    inches = inches % 12

    print("{0} metres and {1} centimetres is equal to {2} feet and {3} inches".format(m, cm, feet, inches))
    
    

def engine():
    decision()

#main program
engine()
