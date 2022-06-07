# Improving with enumerate as previous use of index is less efficient in index searching of every item
current_choice = "-"
computer_parts = []
parts = [
    'monitor',
    'computer',
    'keyboard',
    'mouse',
    'cable'
]
valid_choices = [str(i) for i in range(len(parts) + 1)]

while current_choice != "0":
    if current_choice in valid_choices:
        to_add = parts[int(current_choice) - 1]
        if to_add in computer_parts:
            print(f"Removing {to_add} from computer_parts list")
            computer_parts.remove(to_add)
            print(computer_parts)
        else:
            print(f"Adding {to_add} to computer_parts list")
            computer_parts.append(to_add)
            print(computer_parts)
    else:
        print("Please add option from the list below\n0: exit")
        for position, part in enumerate(parts):
            print(f"{position +1 }: {part}")

    current_choice = input()
print(computer_parts)