"""
This is my claculator program. Ment to take two integers/floats and with a user selected operation
returns a new value as a result. It will detect division by zero errors and repeat if you want to calculater more. Enjoy!
"""

#Imports the math functions
import math

#this is a function that contains my calculator. I have decided to store variables locally, so they can be re-writen.
def calculator():

# Asks the user for two numbers as floats and one operation as a string.
    int_one = float(input ("Please enter your first number: "))
    int_two = float(input ("Please enter your second number: "))
    desired_opp = (input ("Please select an operation "
                          "(+, -, *, /, //, %, **, sqrt, factorial(enter f), sin, cosine, tan: "))

#All the functions below can be called to return the resulting value(s) from the operation.
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    def floor_division(a,b):
        return a//b
    def modulus(a,b):
        return a%b
    def power(a,b):
        return a**b
    def square_root(a,b):
        return math.sqrt(a), math.sqrt(b)
    def factorial(a,b):
        return math.factorial(a), math.factorial(b)
    def sin(a,b):
        return math.sin(a),math.sin(b)
    def cosine(a,b):
        return math.cos(a),math.cos(b)
    def tan(a,b):
        return math.tan(a),math.tan(b)

# Tests the basic functionality of my math functions.
    result = add(-3, 6)
    assert result == 3, f"Expected 3, but got {result}"
    result = subtract(-3, 6)
    assert result == -9, f"Expected -9, but got {result}"
    result = multiply(-3, 6)
    assert result == -18, f"Expected -18, but got {result}"
    result = divide(6, 3)
    assert result == 2, f"Expected 2, but got {result}"
    result = floor_division(7, 7)
    assert result == 1, f"Expected 1, but got {result}"
    result = modulus(6, 4)
    assert result == 2, f"Expected 2, but got {result}"
    result = power(2, 4)
    assert result == 16, f"Expected 16, but got {result}"
    result = square_root(36, 4)
    assert result == (6,2), f"Expected (6,2), but got {result}"
    result = factorial(8, 10)
    assert result == (40320,3628800), f"Expected (40320,3628800), but got {result}"
    result = sin(0,0)
    assert result == (0,0), f"Expected (0,0), but got {result}"
    result = cosine(0,0)
    assert result == (1,1), f"Expected (1,1), but got {result}"
    result = tan(0,0)
    assert result == (0,0), f"Expected (0,0), but got {result}"

# checks if there will be a divide by zero error. If so it will restart the program. desired_opp == "/":
    if int_two == 0 and desired_opp == "/":
        print("Can't divide by zero! Try again!")
        calculator()
    elif int_two == 0 and desired_opp == "//":
        print("Can't divide by zero! Try again!")
        calculator()
    else:
        pass

# Depending on the users input, these if statements will call the functions that corresponds --
# to the users desired input operation
    if desired_opp == "+":
        print(str(int_one)+" + "+str(int_two)+" is: "+ str(add(int_one,int_two)))
    elif desired_opp == "-":
        print(str(int_one)+" - "+str(int_two)+" is: "+ str(subtract(int_one,int_two)))
    elif desired_opp == "*":
        print(str(int_one)+" * "+str(int_two)+" is: "+ str(multiply(int_one, int_two)))
    elif desired_opp == "/":
        print(str(int_one)+" / "+str(int_two)+" is: "+ str(divide(int_one, int_two)))
    elif desired_opp == "//":
        print(str(int_one)+" // "+str(int_two)+" is: "+ str(floor_division(int_one, int_two)))
    elif desired_opp == "%":
        print(str(int_one)+" % "+str(int_two)+" is: "+ str(modulus(int_one, int_two)))
    elif desired_opp == "**":
        print(str(int_one)+" ** "+str(int_two)+" is: "+ str(power(int_one, int_two)))
    elif desired_opp == "sqrt":
        print(str(int_one)+" sqrt "+str(int_two)+" is: "+ str(square_root(int_one, int_two)))
    elif desired_opp == "f":
        print("factorial "+str(int_one)+", factorial "+str(int_two)+" is: " + str(factorial(int_one, int_two)))
    elif desired_opp == "sin":
        print("sin "+str(int_one)+", sin "+str(int_two)+" is: " + str(sin(int_one, int_two)))
    elif desired_opp == "cos":
        print("cos "+str(int_one)+", cos "+str(int_two)+" is: " + str(cosine(int_one, int_two)))
    elif desired_opp == "tan":
        print("tan "+str(int_one)+", tan "+str(int_two)+" is: " + str(tan(int_one, int_two)))
    else:
        print("Something went wrong! try again")
        calculator()

#This calls the calculator function for the first time
calculator()

#This while loop will ask the user if they would like to make another calculation --
#if they would not it ends the program.
#I know we haven't while loops I thought it would be easer to run tests.
while True:
    print ("All tests passed successfully!")
    cont = input(("Want to calculate anything else? (y/n) "))
    if cont == "y":
        calculator()
    else:
        print("Thanks for calculating")
        break
