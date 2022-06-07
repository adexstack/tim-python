available_exits = ["east", "west", "south", "north"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("please choose your exit point\n")
    if chosen_exit.casefold() == "quit":
        print("User quits and Game over")
        break
else:
    print("Welldone! You exit OK. Game over")