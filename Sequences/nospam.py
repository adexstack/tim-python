menu = [
    ["egg", "bacon"],
    ["egg", "spam", "rice"],
    ["spam", "sausage", "cake", "corn"],
    ["egg", "spam", "fish"],
    ]

for lis in menu:
    for index in range(len(lis) - 1, - 1, -1):
        if lis[index] == "spam":
            del lis[index]
    print(lis)
    for item in lis:
        print(item, end=', ') #note that sep keyword will not work here as you onle have 1 object to print (item)
    print()



