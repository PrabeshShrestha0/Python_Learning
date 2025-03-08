# while loop = execurte some code WHILE some conditions remains true
  
# age = int(input("enter age:"))

# while age < 0:
#     print("you didnot entered the valid age")
#     age = int(input("please enter the age:"))
# print(f"Your age is {age}")



# Now doing the same code with not and or

# age = int(input("enter age:"))

# while not (age > 0 and age < 18):
#     print("you didnot entered the valid age")
#     age = int(input("please enter the age:"))
# print(f"Your age is {age}")

# now for or
# while not (age > 18 or age < 0):
#     print("you didnot entered the valid age")
#     age = int(input("please enter the age:"))
# print(f"Your age is {age}")



# Exercise to make a compound interest calculator


# Initialize variables
# principal = 0
# rate = 0
# time = 0

# # Input validation for principal
# while principal <= 0:
#     principal = float(input("Enter the principal: "))
#     if principal <= 0:
#         print("You cannot enter a value less than or equal to 0. Please try again.")

# # Input validation for rate
# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("You cannot enter a value less than or equal to 0. Please try again.")

# # Input validation for time
# while time <= 0:
#     time = int(input("Enter the time (years): "))
#     if time <= 0:
#         print("You cannot enter a value less than or equal to 0. Please try again.")

# # Calculate the amount using compound interest formula
# Amount = principal * pow((1 + rate / 100), time)

# # Display the result
# print(f"Your total balance amount is: ${Amount:.2f}")
