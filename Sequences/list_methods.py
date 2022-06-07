empty_list = []
even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

more_numbers = numbers.copy()
print(more_numbers)

print(numbers is more_numbers) # checking for variable equality (ids)
print(numbers == more_numbers) # checking for content equality in order

digits = list("432985617") # converting string to list
print(digits)

slice_copy = numbers[:]
print(slice_copy)

slice_copy_sub = numbers[:4]
print(slice_copy_sub)

print("-------------Replacing list items----------")
parts = ["ace", "can", "cup", "jug"]
parts[2] = "book"
print(parts)
parts.insert(1, "Phone") # would shift existing list item to the right
print(parts)
parts[1:3] = ["plug", "cable"]
print(parts)