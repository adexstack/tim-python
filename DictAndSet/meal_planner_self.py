from contents import recipes, pantry

# print(recipes)

display_dict = {str(index + 1): value for index, value in enumerate(recipes)}
print(display_dict)


required_pantry = {}


def get_required_pantry(required_key, required_value):
    """
    Adding items to a dictionary
    :param required_key: key
    :param required_value: value
    """
    required_pantry[required_key] = required_value


while True:
    # Displaying menu
    print("Please choose your menu")
    print("-----------------------")
    for key, value in display_dict.items():
        print(key, value)
    choice = input("> ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients..............")
        ingredients = recipes[selected_item]
        print(ingredients)
        missing_pantry = {}
        for food_item, required_quantity in ingredients.items():
            if required_quantity > pantry.get(food_item, 0):
                deficit = required_quantity - pantry.get(food_item, 0)
                required_pantry[food_item] = deficit
                get_required_pantry(food_item, deficit)
        print(f"Required Pantry Items: {required_pantry}")

