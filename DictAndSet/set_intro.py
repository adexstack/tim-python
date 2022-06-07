# set are unordered
farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}

print(farm_animals)

for animal in farm_animals:
    print(animal)

farm_animals_reordered = {'cow', 'horse', 'hen', 'goat', 'sheep'}

print(farm_animals == farm_animals_reordered) # world print True as set doesn't care about order; just content