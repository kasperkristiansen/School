from math import sqrt
user = True
elements = []

num1 = float(input("Enter a number: "))
op = str(input("Enter operator: "))
num2 = float(input("Enter another number: "))

if op == "*":
    print("Total: ", num1 * num2)
elif op == "/":
    print("Total: ", num1 / num2)
elif op == "-":
    print("Total: ", num1 - num2)
elif op == "+":
    print("Total: ", num1 + num2)
elif op == "%":
    print("Total: ", num1 % num2)
elif op == "sqrt":
    print("Total: ", sqrt(num1), sqrt(num2))
elif op == "pow":
    print(pow(num1, num2))
