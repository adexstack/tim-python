from contents import recipes

print(recipes)


def my_deepcopy(d: dict) -> dict:
    """
    Copy a dictionary, creating a copy of the 'list' or 'dict' values.

    The function will crash with and AttributError if the values are not list or dictionary
    :param d: The dictionary to copy
    :return: A copy of 'd' , with the values been copied off the original values.
    """
    new_dic = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dic[key] = new_value
    return new_dic


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])