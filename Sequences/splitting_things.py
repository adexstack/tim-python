# returns list separated by either the default white space or provided separator
panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
split_numbers = numbers.split(",") # converting to list
print(type(split_numbers))
print(split_numbers)
join_split_items = ", ".join(split_numbers) # removing enclosing '' and converting back to string
print(type(join_split_items))
print(join_split_items)

# separators = ", "
# generated_list = ", ".join(char for char in numbers).split()
# print(generated_list)
print("-------------------------------------------------------------")

generated_list = ['9', ' '
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']

# join at white space
values = "".join(generated_list)
print(values)

# split at white space in the string to produce list
values_list = values.split()
print(values_list)

print("-----------------------------")
for item in values_list:
    items = ", ".join((item for item in values_list))
print(items)
