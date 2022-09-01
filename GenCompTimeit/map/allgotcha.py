entries = []

if entries:
    print("all: {}".format(all(entries)))
else:
    print(False)
print("any: {}".format(any(entries)))


#gotcha: would print empty list
result = entries and all(entries)
print(result)

# You need to be explicit using bool(entries)
result = bool(entries) and all(entries)
print(result)
