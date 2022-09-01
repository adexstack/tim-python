from data import people, plants_list, plants_dict

# people = []

if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

print("-" * 20)
#Use any and a comprehension (or generator expression, if you prefer) to check the plants in plants_dict to see if
# there are any grasses in there.

# using generators here () not list []
if any(plantDetails.plant_type == "Grass" for plantDetails in plants_dict.values()):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

# Run your code again, searching for Cactus, to test that it still works when there aren't any.

if any(plantDetails.plant_type == "Cactus" for plantDetails in plants_dict.values()):
    print("This pack contains cactus")
else:
    print("No cactus in this pack")