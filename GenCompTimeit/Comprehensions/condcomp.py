menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)
print('*' * 30)
print([meal for meal in menu if "spam" not in meal])

# both are also valid
print([meal for meal in menu if "spam" not in meal if "chicken" not in meal])
print([meal for meal in menu if "spam" not in meal and "chicken" not in meal])

fussy_meals = [meal for meal in menu if
               ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]  # <--
print(fussy_meals)
