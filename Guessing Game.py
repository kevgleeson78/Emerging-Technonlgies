# Guessing Game for python
import random
correct = False
attempt = 0
secret_number = random.randint(1, 100)

while not correct:
    print(attempt)
    guess = int(input("Please guess a number between 1 - 100\n"))
    if guess > secret_number:
        print("that is too high...")
        attempt +=1
    if guess < secret_number:
        print("that is too low...")
        attempt +=1
    if guess == secret_number:
        print("Well done you have guessed correctly!!!")
        print("The total amount of attempts taken...", attempt)
        break

