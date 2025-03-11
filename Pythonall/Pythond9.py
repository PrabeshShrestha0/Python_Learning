# nested loop = loop within a loop
# outer loop = loop that contains the inner loop
# inner loop = loop that is contained within the outer loop
# outer loop:
#     inner loop:

# for x in range(3):
#     for c in range(1,10):
#         print(c, end="")
#     print()


# rows = int(input("Enter the # of rows:"))
# coloumns = int(input("Enter the # of coloumns:"))
# symbol = input("Enter the symbol to use:")

# for x in range(rows):
#     for c in range(coloumns):
#         print(symbol, end="")
#     print()



# collection = single varaible that are used to store multiple varaibles
# collection = list, tuple, set, dictionary, etc.
# list = ordered collection of items [] ordered and changeable Duplicates ok
# tuple = ordered collection of items () ordered and unchangeable Duplicates ok
# set = unordered collection of items {} unordered and unchangeable Duplicates not ok
# dictionary = unordered collection of items {} unordered and changeable Duplicates ok


fruits = ["Apple","Banana","Watermelon"]

# # print(fruits[0])

# for fruits in fruits:
#     print(fruits)
# print(fruits)
fruits.append("rose") # add to the end of the list
print(fruits)
print("lily" in fruits) # returns true if the item is in the list, false if not
print("rose" in fruits) # returns true if the item is in the list, false if not
print(len(fruits)) # returns the # of items in the list
print(fruits.count("apple"))
print(fruits.remove("rose"))
print(fruits.sort())
print(fruits.count("Watermelon")) # returns the list in sorted order
print(fruits.index("Watermelon")) # returns the index of the item in the list
print(fruits.pop()) # removes the last item in the list and returns it
print(fruits.clear())