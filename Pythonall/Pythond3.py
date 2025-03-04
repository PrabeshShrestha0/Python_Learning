# calculate hypotaneus to calculate of right angle traingle

# import math
# value_a = float(input("Enter the value of a: "))
# value_b = float(input("Enter the value of b: "))
# hypotenuse = math.sqrt((value_a**2)+(value_b**2))
# print(f"The hypotenuse value of the given right angle triangle is: {round(hypotenuse)}")

# Make a calculator that can add, subtract, multiply, and divide

# Calc = input("Hello, I am the calculator. It's a pleasure to help you.\nEnter what would you like to perform:\n A for Addition\n S for Subtraction\n M for Multiplication\n D for Division\n (A/S/M/D): ")
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# if Calc == "A":
#     Add = num1 + num2
#     print(f"The addition of your numbers is: {Add}")

# elif Calc == "S":
#     Sub = num1 - num2
#     print(f"The subtraction of the given numbers is: {Sub}")

# elif Calc == "M":
#     Mul = num1 * num2
#     print(f"The multiplication of your numbers is: {Mul}")

# elif Calc == "D":
#     Div = num1 / num2
#     print(f"The division of given number is: {Div}")

# else:
#     print("You give invalid input Please Give valid input next time")

# Python weight converter

weight = float(input("Enter your weight: "))
unit = str(input("Enter your unit (kg/pound): "))

if unit == "kg":
    weight = weight * 2.205
    print(f"Your weight in pounds is: {round(weight)} lbs")

elif unit == "pound":
    weight = weight / 2.205
    print(f"Your weight in kg is: {round(weight)} kg")

else:
    print("Invalid input")
