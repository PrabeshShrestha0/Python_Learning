# indexing = Accessing elements in a list or sequence by their index []

Prabesh = "1233-566643"
# print(Prabesh[10]) This will print the 11th character of the string Prabesh and index usually starts counting from 0 1 2 3 4 ..... n
# print(Prabesh[0:5]) This will print the first 5 characters of the string Prabesh
# print(Prabesh[0:10])
# print(Prabesh[-1]) This will print the last character of the string Prabesh
# print(Prabesh[::3]) This will print every 3rd character of the string Prabesh

# Exercise to get last four number of credit card number

# card = "1234-1243-4566-2345"
# number = card[-4:]
# print(f"xxxx-xxxx-xxxx-{number}")

# This will print the last 4 characters of the string card


# format specifiers = Used to format the output of a string
# {value:flag}


price1 = 9080.90
price2 = -123.45
price3 = 0.009

# .(number)f = round to that decimal places 
# print(f"The price is ${price1:.2f}")
# print(f"The price is ${price2:.2f}")
# print(f"The price is ${price3:.2f}")

# (:number) This will create the total space 10
# and if we put 0 in the space it will be 0 padded/added that is given in second example down
# print(f"The price is ${price1:10}")
# print(f"The price is ${price2:10}")
# print(f"The price is ${price3:10}")

# print(f"The price is ${price1:010}")
# print(f"The price is ${price2:010}")
# print(f"The price is ${price3:010}")

# (:<number) This will left justify the number
# print(f"The price is ${price1:<10}")
# print(f"The price is ${price2:<10}")
# print(f"The price is ${price3:<10}")

# (:>number) This wil justify the number at right
# print(f"The price is ${price1:>10}")
# print(f"The price is ${price2:>10}")
# print(f"The price is ${price3:>10}")

# (:^number) This will center the number
# print(f"The price is ${price1:^10}")
# print(f"The price is ${price2:^10}")

# (:+) This will add the sign to the number it means it shows positive if the number is + and negative if the number is -
# print(f"The price is ${price1:+}")
# print(f"The price is ${price2:+}")
# print(f"The price is ${price3:+}")