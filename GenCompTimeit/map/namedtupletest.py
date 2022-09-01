from data import basic_plants_list, plants_list

print(plants_list[0])

# for plant in basic_plants_list:
#     print(plant[0])

for plant in plants_list:
    # using .notation or index (Note this is contrived as mixing both is not recommended) use either .field or index
    print(plant.name, plant[1])

print()

example = plants_list[0]
print(example)
# _replace is one of the 3 extra functions in named tuple that doesn't exist in ordinary tuple
example = example._replace(lifecycle='Annual')
print(example)
