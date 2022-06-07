lis = [5, 7, 7, 21, 30]

for num in lis:
    if num % 8 == 0:
        print("That number should not be in the list")
        break
else:
    print("Great! There is no 8 divisible number in the list")