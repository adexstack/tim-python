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
integer_values = []
items = [integer_values.append(int(item)) for item in values_list]
print(integer_values)