# main.py

from calculator.calculator_wrapper import calculate

num_one = int(input("Enter your first number: "))
num_two = int(input("Enter your second number: "))
num_three = int(input("Enter your third number: "))

print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
choice = int(input("Enter your choice: "))

result = calculate(num_one, num_two, num_three, choice)
print("The result is:", result)
