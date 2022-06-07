available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }


chosen_new_part = {}
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
        chosen_new_part[current_choice] = chosen_part
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(key, value, sep=", ")
        print("0: to finish")
    current_choice = input("> ")

print("----new added item-----")
for key, value in chosen_new_part.items():
    print(key, value, sep=", ")