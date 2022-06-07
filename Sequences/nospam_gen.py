menu = [
    ["egg", "bacon"],
    ["egg", "spam", "rice"],
    ["spam", "sausage", "cake", "corn"],
    ["egg", "spam", "fish"],
    ]

# optimized of nospam.py removing spam from all menu list and creating lists
for meal in menu:
    items = [item for item in meal if item != "spam"]
    print(items)

print("-------optimized of nospam.py using generators and removing trailing commas------")
for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)




