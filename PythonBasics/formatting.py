for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
    print(f"No. {i} squared is {i ** 2} and cubed is {i ** 3}")

# Left aligned. Adding :<width> for alignment ; the string takes up the whole width and blank where is not filled
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
print()

# Right aligned.
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
print()

# Center aligned. Adding :<width> for alignment ; the string takes up the whole width and blank where is not filled
for i in range(1, 13):
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
print()

print("Pi is approximately {0:12}".format(22 / 7)) # width overide to 15 decimal places
print("Pi is approximately {0:12f}".format(22 / 7)) # 6 default decimal places
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7)) # allowed only up to 51 places, last 3 filled with 000
print()

# can remove the index if not needed and still use the width
for i in range(1, 13):
    print("No. {:2} squared is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))
print()

# Using f string (supported from Python 3.6)
age = 2
print('name' + f" is {age} years old")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")