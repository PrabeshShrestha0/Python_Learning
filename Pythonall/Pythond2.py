#  input() it ask a prompt from a user to enter the darta and return it into string

# Prabesh = str(input("Enter your name:")) 
# Age = int(input("Enter your Age:")) 
# print(f"i got it your name is {Prabesh} and Many Happy Returns of the day {Prabesh}")
# print(f"Now you are {Age} years old and i am happy to know that") # it will throw an error because we are trying to print an integer


# Exercise to calsulate area of rectangle

# Area = int(input("Enter the Length:"))
# Area2 = int(input("Enter the breadth:"))
# Area3 = Area * Area2
# print(f"Area of rectangle is {Area3}")


# Exercise 2 shopping cart Program

# item = input("what item do you want ot buy?:")
# price = float(input("What is the price?: "))
# quantity = int(input("how many would you like to buy:"))
# total = price * quantity
# print(f"you have to pay {total} for {item}")

# Exercise 3 Madlibs game where you create a story by filling in blanks with random words
# Guess about her and why do you like her?
# description = input("Enter how she looks like:")
# description2 = input("Enter her personality:")
# description3 = input("Enter her another best personality:")
# description4 = input("Enter what she takes of you:")
# description5 = input("Enter what she always do till death:")
# print("I love her because:")
# print(f"she is {description}.")
# print(f"she is {description2} and {description3} ")
# print(f"The world doesnot {description4} about me but she will always {description4} about meand {description5} me")

# Builtin math functions
# round() 3.223 to 3
# abs() -4 to 4
# pow(2,3) 2 to the power of 3 = 8  (2*2*2)
# max() 2,3,4 = 4
# min() 2,3,4 = 2


# import math

# x = 4.1
# print(math.pi)
# print(math.e)
# result = math.floor(x) it will round down the number
# result = math.ceil(x) # it will round up the number and return the integer
# result = math.sqrt(x) # it will return the square root of the number
# print(result)


# Exercise to calculate Circumference of circle using math functions

# import math
# r = int(input("Enter the radius:"))
# pie = math.pi
# circumference = 2 * pie * r
# print(f"The circumference of the circle is {round(circumference,3)}")


# Exercise to calculate area of circle using math functions

# import math
# r = float(input("Enter the radius:"))
# area_of_circle = math.pi * (r**2)
# print(f"The area of the circle is {round(area_of_circle,3)}")  # round


# calculate hypotaneus to calculate of right angle traingle

# import math
# value_a = float(input("Enter the value of a"))
# value_b = float(input("Enter the value of b"))
# Hypotaneus = math.sqrt((value_a**2)+(value_b**2))
# print(f"The hypotaneus value of given rightangle triangle is: {round(Hypotaneus)}")

# Make a calculator that can add subtract and divide and Multlipy


# Calc = input("Hello , I am the calculator It's pleasure to help you\nEnter what would you like to perform:\n A for Addition\n S for Subtraction\n M for Multiplication\n D for Division\n (A/S/M/D):")
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# if Calc == "A":
#     Add = num1 + num2
#     print(f"The addition of your number is:{Add}")

# elif Calc == "S":
#     Sub = num1 - num2
#     print(f"The subtraction of given number is: {Sub}")

# elif Calc == "M":
#     Mul = num1 * num2
#     print(f"The multiplication of given number is: {Mul}")

# elif Calc == "D":
#     Div = num1 / num2
#     print(f"The division of given number is: {Div}")

# else:
#     print("You give invalid input Please Give valid input next time")

