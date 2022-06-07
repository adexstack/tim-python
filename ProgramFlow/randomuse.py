import random

highest = 10
answer = random.randint(1, 10) # 1 - 10 inclusive

print(f"please guess a number between 1 and {highest} or 0 to quit")
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("Welldone")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

