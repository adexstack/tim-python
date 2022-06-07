current_choice = "-"
computer_parts = []
parts = [
    'monitor',
    'computer',
    'keyboard',
    'mouse',
    'cable'
]

while current_choice != "0":
    if current_choice in "12345":
        print(f"Adding {current_choice} to list")
        if current_choice == "1":
            computer_parts.append("monitor")
        elif current_choice == "2":
            computer_parts.append("computer")
        elif current_choice == "3":
            computer_parts.append("keyboard")
        elif current_choice == "4":
            computer_parts.append("mouse")
        elif current_choice == "5":
            computer_parts.append("cable")
    else:
        print("Please add option from the list below\n0: exit")
        for part in parts:
            print(f"{parts.index(part) +1 }: {part}")

    current_choice = input()
print(computer_parts)