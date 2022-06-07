numbers1 = {*""}
numbers2 = {*{}}

# print(numbers1, type(numbers1))
# print(numbers2, type(numbers2))

numbers = set()
while len(numbers) < 4:
    next_value = int(input("Please enter your next value "))
    numbers.add(next_value)
print(numbers)