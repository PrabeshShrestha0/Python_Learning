# conditional statement : it is one line shortcut for the if else statement (Ternary operator)
# syntax : value_if_true if condition else value_if_false
# example : x if condition else y

# num = 5
# a = 7
# b = 3
# age = 18
# role = "user"
# print("Positive" if num > 0 else "Negative")  # Output: Positive

# max_num = a if a > b else b
# min_num = a if a < b else b

# status = "Adult" if age >= 18 else "Minor"
# print(status)
# acess = "Provide acess" if role == "admin" else "No acess"
# print(acess)  # Output: Provide acess



# String
# String is a collection of characters

# name = input("Enter your name: ")
# result = name.find("b") this will find the character of string where it is located and it currently checks from 0 to count
# result = name.rfind("a") This is the reverse finding
# print(f"Your {name} length is: {len(name)} ")
# result = name.capitalize() This will capitalize the first letter of the string
# result = name.upper() This will uppper case the string
# result = name.lower() This will lower case the string
# result = name.isalpha() This checks is the string is alphabet or not
# result = name.isdigit() This will check if the string is digit or not
# result = phone_number.count("-") THis will count the - in phone number
# result = phone_number.replace("-"," ") This will replace the - with nothing
# print(result)

# To know all the methods of strings you need to type
# help(str) in python

# print(help(str))


# Exercise 

# validation of user input 
# 1 username is no more than 12  chatracters 
# username must not contain spaces
# username must not contain digits

# username = input("Enter user name:")
# username.find(" ")

# len(username)
# if len(username) > 12:
#     print("username is too long")
# elif not username.find(" ") == -1:
#     print("username shouldnot contain spaces")
# elif not username.isalpha():
#     print("Your name must not contain digits")
# else:
#     print(f"WELCOME {username}")




