from primes_and_squares import squares_generator, primes_generator

#seta = {i for i in range(1, 11, 2)}

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.intersection(squares))
print(evens & squares)

# intersection accepts any iterable (operator only accept object and set)
even_squares = evens.intersection(squares_generator(100))
print(even_squares)