age = int(input("How old are you? "))
if age > 18:
    print("You are really old")
elif age == 18:
    print("Just spot on")
else:
    print(f"Come back in {18 - age} years' time")

x = 5
y = 7
if x < y:
    print("{} is smaller than {}".format(x, y))
elif x > y:
    print("{} is greater than {}".format(x, y))
else:
    print("{} equals {}".format(x, y))