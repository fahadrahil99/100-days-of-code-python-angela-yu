def add(n1, n2):
    return n1 + n2
def subtract(n1 , n2) :
    return  n1 - n2
def multiply(n1 , n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {"+":add,
              "-":subtract,
              "*":multiply,
              "/":divide,
            }
import art
def calculator():
    print(art.logo)
    whether_to_continue = True
    number1 = float(input("What is the first number?: \n"))
    while whether_to_continue:
        for key in operations:
            print(key)
        operator1 = input("Pick an operation: \n")
        number2 = float(input("What is the next number?: \n"))
        result = float(operations[operator1](number1,number2))
        print(f"{number1} {operator1} {number2} = {result}")
        to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()



        if to_continue == "y":
            number1 = result
        else:
            whether_to_continue = False
            calculator()

calculator()








