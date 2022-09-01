def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)
    comparison_count = 0

    # looping items up to the one but last
    for i in range(n - 1):
        # inner llop: looping items up to the one but last
        for j in range(n - 1):
            # increasing count + 1 for every comparison performed
            comparison_count += 1
            # if current item is greater than next, swap the items around (sorting)
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

        print(f"End of pass {i}.  `data` is now {data}")
    print(f"comparison_count is {comparison_count}")


numbers = [3, 2, 4, 1, 5, 7, 6]

print(f"Sorting {numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")

# x = 1
# y = 2
# print(x, y)
#
# x, y = y, x
# print(x, y)