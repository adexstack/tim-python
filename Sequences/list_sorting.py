even = [2,4,6,8]
odd = [1,3,5,7]

even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort(reverse=True)
print(even)
print(another_even)
print()
forward_sort = even.sort()
print(forward_sort) # None as it sorts in place
print(even)
forward_sort = even
print(forward_sort)