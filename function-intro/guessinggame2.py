import random

# improved and optimized. else not required after return


def get_integer(prompt):
    """
        Get an integer from Standard Input (stdin).

        The function will continue looping, and prompting
        the user, until a valid `int` is entered.

        :param prompt: The String that the user will see, when
            they're prompted to enter the value.
        :return: The integer that the user enters.
        """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print(f"{temp} isn't a valid integer, please enter integer")


highest = 1000
answer = random.randint(1, highest) # 1 - 1000 inclusive
guess = 0
print(f"please guess a number between 1 and {highest} or 0 to quit")

while guess != answer:
    guess = get_integer(": ")

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

