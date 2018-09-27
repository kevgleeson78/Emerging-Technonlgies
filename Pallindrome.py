# Python problem sets

user_word = input("Pleases enter a word")

reverse_word = user_word[::-1]

print(reverse_word)

if user_word == reverse_word:
    print("This is a palindrome!!")
else:
    print("this is not a palindrome!!")