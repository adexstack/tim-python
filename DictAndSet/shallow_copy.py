animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

# things and animals are the same object since their items are immutable
things = animals
print(id(things))
print(id(animals))
print(things is animals)
print(things)
print(animals)
animals["teddy"] = "toy"
print(animals["teddy"])
print(things["teddy"])

print()
things = animals.copy()
animals["teddy"] = "mouse"
print(animals["teddy"])
print(things["teddy"])
