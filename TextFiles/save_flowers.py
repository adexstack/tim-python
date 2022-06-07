data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

plants_filename = "flowers_print.txt"

# with open(plants_filename, 'w') as plants:
#     for plant in data:
#         print(plant, file=plants)
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
#
# print(new_list)

# with open(plants_filename, 'w') as plants:
#     for plant in data:
#         plants.write(plant)
#
# new_list = []
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
# print(new_list)
#
# with open(plants_filename, "w") as plants:
#     for plant in data:
#         plants.write(plant)
# print(data)
#
# string_representation = data.__str__()
# print(type(string_representation))

# .write() only allows the string representation of data, does not allow number, only string
filename = "test_numbers.txt"
# with open(filename, 'w') as test:
#     for i in range(10):
#         print(i, file=test)


# with open(filename, 'w') as test:
#     for i in range(10):
#         test.write(i) # This would give TypeError
#         test.write(str(i)) # This would write all numbers in one line. write only writes whatever its given
#         test.write(str(i) + "\n") This would write on separate lines

