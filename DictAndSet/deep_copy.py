#Deep copy copies the actual mutable object and not just the reference
import copy
animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# shallow copy (original dict contains mutable items)
#things = animals.copy()

# Deep copying
things = copy.deepcopy(animals)

print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
