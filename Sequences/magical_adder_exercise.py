user_input = input("Please enter three numbers similar to: 10,11,10\n")
split_input = user_input.split(",")
int_convert = [int(dig) for dig in split_input]
print(int_convert)
print(int_convert[0] + int_convert[1] - (int_convert[2]))
