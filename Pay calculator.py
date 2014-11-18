#Ryan Cox
#18/11/14
#calculate pay

def calculate_basic_pay(hours,pay):
    total_basic_pay = hours * pay
    return total_basic_pay


def calculate_overtime_pay(hours,pay):
    overtime_hours = (hours - 39)
    total_basic_pay = (hours - overtime_hours) * pay    
    total_overtime_pay = overtime_hours * (pay * 1.5)
    total_pay = total_overtime_pay + total_basic_pay 
    return total_pay


def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)  
    else:
        total = calculate_overtime_pay(hours,pay)        
    return total

##def input_info:
 ##pay = int(input("Please enter your basic pay: "))
 ##hours = int(input("Please enter the hours you worked: "))

#Main program



pay = calculate_total_pay(42,1.)

print("your total pay is £{0}".format.__call__(pay))
