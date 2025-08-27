from operator import truediv
from art import *
print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
output =""

def calculator():
     Calculate_again = True
     value1 = float(input("Enter your first value: "))




     while Calculate_again:
         operation = input("Enter your operation:+, -, * or / ")
         value2 = float(input("Enter your second value: "))
         output = operations[operation](value1, value2)
         print(f"{value1} {operation} {value2} = {output}")

         ask = input("Do you want to continue with the present calculation? (y/n): ")
         if ask == "y":
             calculate_again = True
             value1 = output
         if ask == "n":
             calculate_again = False
             print("\n" * 20)
             calculator()

calculator()
