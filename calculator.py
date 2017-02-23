"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

list1 = [1, 2, 3]

from our_arithmetic import *

# add print statement of user equation options like + - pow and in prefix style
def user_input():
    user_equation = raw_input("Enter the operation followed by the numbers you'd like to perform: ")
    tokenize_equation = user_equation.split(" ")
    operator = tokenize_equation[0]
    num1 = int(tokenize_equation[1])
    num2 = int(tokenize_equation[2])


    while True:
        if tokenize_equation[0] == "+":
            print add(num1, num2)

        if tokenize_equation[0] == "-":
            print subtract(num1, num2)

        if tokenize_equation[0] == "*":
            print multiply(num1, num2)

        if tokenize_equation[0] == "/":
            print divide(num1, num2)        

        if tokenize_equation[0] == "%":
            print mod(num1, num2)

        if tokenize_equation[0] == "**":
            print power(num1, num2)
            
        # if tokenize_equation[0] == "+":
        #     print add(num1, num2)

        # if tokenize_equation[0] == "+":
        #     print add(num1, num2) 

user_input()


