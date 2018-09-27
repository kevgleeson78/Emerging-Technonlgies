# Reverse a string with python

user_input = input("Please enter a word to reverse...\n")

reverse_word = user_input[::-1]

print("the reversed word is..." + reverse_word)


def reverse(func_input):
    new_reverse = func_input[::-1]
    return new_reverse


print(reverse(user_input))
