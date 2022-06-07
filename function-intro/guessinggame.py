import random

highest = 1000
answer = random.randint(1, highest) # 1 - 1000 inclusive

guess = 0
print(f"please guess a number between 1 and {highest} or 0 to quit")

while guess != answer:
    try:
        guess = int(input())
    except ValueError:
        print("Please enter an integer value")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")

