for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("please choose exit direction: ")
print("Bet you are glad to be out")