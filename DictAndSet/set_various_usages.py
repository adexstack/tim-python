scorpions = {"emporor", "red claw", "arizon", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"trantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}
mini_vespas = {"paper wasp", "hornet", "can"}


print(scorpions.union(snakes))
print(scorpions | snakes)
print(len(vespas))
print("seyi" not in vespas)
print(spiders.isdisjoint(vespas)) # True if their intersection is empty (No common element)
print(mini_vespas.issubset(vespas)) # Test whether every element in the mini_vespas is in other.
print(vespas.issuperset(mini_vespas)) # Test whether every element in vespas is in the set.
print(vespas.union(mini_vespas)) # Return a new set with elements from the set and all others.
print(vespas.intersection(mini_vespas))
print(vespas.difference(mini_vespas))
print(vespas.symmetric_difference(mini_vespas)) # what is in vespas and not in mini_vespas & vice versa
print((mini_vespas.copy()))

print("-------------------")
new_set = set()
for anim in scorpions:
    new_set.update(anim)
    #print("updating with "+ anim)


