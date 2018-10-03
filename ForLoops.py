# We can use range in a for loop to create a list
# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in l:
# The above for loop declaration can be changed to range to auto create a list

for i in range(20):
    # To format Strings in python see below
    # They are are f strings
    print(f"{i:2} {i*i:4}")

# This will print out the first and last element in the list
print(range(20))

# This will print out the entire list
# Generaters can be used to only select certain items in a list
print(list(range(20)))
print("That's the whole list..")