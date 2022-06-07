#list dict set Bytearray  The ids remain unchanged

lis_a = ["ant", "can", "dan"]
another_list = lis_a
print(lis_a)
print(id(lis_a))
print(another_list)
print(id(another_list))

lis_a += ["fan"]
print(lis_a)
print(id(lis_a))
print(another_list)
print(id(another_list))

a = b = c = d = e = another_list
print(a)
b.append("cream")
print(c)
print(d)
print(e)
print(a)