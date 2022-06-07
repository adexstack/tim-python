parrot = 'Norwegian Blue'
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
print()
# using negative index
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print(parrot[:6] + parrot[6:])
print(parrot[:])

itemsList = ["ken", "dan", "tuj"]
print(itemsList[:].__len__())

number = "9,223:372;036 854:775,807"
separators = (number[1::4])
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

# slice back
letters = 'abcde'
print(letters[::-1])

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-10:-13:-1])
print(letters[-22::-1])

# last 8 letters
print(letters[:-9:-1])
print(letters[25:-9:-1])

last_4_letters = (letters[-4:])
print(last_4_letters)

print(letters[-1:]) # print z
print(letters[:1]) # print a
print(letters[0])  # print a

empty = ""
print("I am" + empty[:1]) # print empty sequence
print(empty[0])  # IndexError

# prints MTWTFSS; slice starts from 1st character , and includes every 5th character
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])