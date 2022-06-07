flowers = [
    "Daffodil",
    "Evening Primrose",
    "Iris",
    "Sunflower",
    "Lavendar",
]

for flower in flowers:
    print(flower)

# using the string method join. Note that all the items in the iterables must be string to use the join method
separator = " | "
output = separator.join(flowers)
print(output)
