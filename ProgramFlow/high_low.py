import random

# Binary search (Binary chop)
# The most efficient way of finding an item in an ordered list
# it forms the basis for data structures that database programs use in storing database keys
# low + (high - low)//2

low = 1
high = 1000
print(f"I have a number in mind you have to get with max of 10 guesses; Choose a number between {low} and {high} ")
input("Press ENTER to start ")

guesses = 0
while True:
    print(f"\tGuessing in the range of {low} and {high}")
    guess = low + (high - low) // 2
    guesses += 1
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes 1 less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, or c")
