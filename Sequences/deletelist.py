data = [4, 5, 10, 20, 30, 100, 120, 150]

# del data[0:2]
# print(data)
# del data[4:]
# print(data)

min_valid = 10
max_valid = 100

# This would not work as expected as index target changes after item is deleted
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         print(f"deleting {value} at {index}")
#         del data[index]
#         print(data)
# print(data)

stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)  # for debugging
del data[:stop]
print(data)

start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # We have the index of the last item to keep
        # Set 'Start' to the position of the first
        # item to delete, which is 1 after 'index'
        start = index + 1
        break
print(start) # for debugging
del data[start:]
print(data)
