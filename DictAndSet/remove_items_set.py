small_ints = set(range(21))
print(small_ints)

#small_ints.clear()

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99) # would NOT cause keyError if item not exist
print(small_ints)

small_ints.remove(95) # would cause stack trace KeyError if item not exist
print(small_ints)