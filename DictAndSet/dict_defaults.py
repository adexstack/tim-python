from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

# would create a dictionary entry with the default key, value if key doesn't exist
beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

# does not create a dictionary entry with the default key
ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini: {z_quantity}")

print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)
