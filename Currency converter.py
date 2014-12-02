#Ryan Cox
#02/12/14
#Currency converter

def information():
    print("Please enter the currency you have out of: GBP, USD or EURO: ")
    currency = input("Please enter the currency you have that you wish to convert: ")
    amount = int(input("how much do you have?"))
    return currency, amount

def choice(currency, amount):
    if currency == "GBP":
        converterGBP(amount)
        

    elif currency == "USD":
        converterUSD(amount)
        

    elif currency == "EURO":
        converterEURO(amount)
    
    

def converterGBP(amount):
    USD = amount * 1.601
    Euro = amount * 1.229
    return Euro, USD
    

def converterUSD(amount):
    USD = amount * 0.625
    Euro = amount * 0.768
    return Euro, USD
    

def converterEURO(amount):
    USD = amount * 0.814
    Euro = amount * 1.302
    return Euro, USD
    

def output(Euro, USD):
    print("You have {0} USD or {1} Euro".format(USD, Euro))


def engine():
    currency, amount = information()
    choice(currency, amount)
    output(USD, Euro)

#main program

engine()


    
