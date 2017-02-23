"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from our_arithmetic import *


def oops_check():
    user_equation = raw_input("Enter the operation followed by the numbers you'd like to perform: ")
    tokens = user_equation.split(" ")
    try:
        operator = tokens[0]
        return operator
        
    except (ValueError, NameError, RuntimeError, IndexError):
        print "You've entered an invalid thing. Try again, c'mon man!"
        return oops_check()
    return user_input(operator, tokens)


# add print statement of user equation options like + - pow and in prefix style
def user_input(operator, tokens):

    while True:
        
        # enables user to quit
        if operator == "q":
            break

        # enables user to use the arithmetic functions  
        if operator == "+":
            print add(int(tokens[1]), int(tokens[2]))

        elif operator == "-":
            print subtract(int(tokens[1]), int(tokens[2]))

        elif operator == "*":
            print multiply(int(tokens[1]), int(tokens[2]))

        elif operator == "/":
            print divide(int(tokens[1]), int(tokens[2]))        

        elif operator == "%":
            print mod(int(tokens[1]), int(tokens[2]))

        elif operator == "**":
            print power(int(tokens[1]), int(tokens[2]))
            
        elif operator == "**2":
            print square(int(tokens[1]))

        elif operator == "**3":
            print cube(int(tokens[1])) 

        else:
            print "You've entered an invalid operation."

oops_check()



