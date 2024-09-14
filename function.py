# in Python , functions are block of reusable codes that performs a specific task.
# they help make your code organised and modular
# a function is defined using the def
# keyword, followed by the function name and parameter(optional)


# def greeting():
#     print("Welcome to python class")

# greeting()

# def greetinTwo():
#     print("Happy holidays to you")

# greetinTwo()

# print("Outside Fuction")


# first = 20
# second = 60

# def addition():
#     sum = first + second
#     print(f" the addition of {first} and {second} is {sum}")

    
# addition()

# functiions with parameter

# def greeting(firstname, lastname ):
#     print(f"Good Morning {firstname} {lastname}")

# greeting("Ugo","Paul")


# def favourite(food):
#     print(f"my favourite food is {food}")

# favourite("egusi")

# create function to calculate any age

# def appCalculator(year):
    
#     age = 2024 - int(year)

#     print(f"your age is {age}")

# appCalculator(1989)


## Calculate simple interest

 # interest = (principal * rate * time) / 100

 # total repayment = interest + principal

 # total repayment amount for a a load on BTbank

rate = 2.5

def totalLoanPayment():

    principal = input("Kindly enter your loan amount")

    time = input("How many years would you like to clear your loan")

    principal = float(principal)
    time = float(time)

    interest = (principal * rate) / 100

    totalamount = interest + principal

    print(f"Your total repayment for loan of {principal} duration {int(time)} years in ${totalamount}")

totalLoanPayment()