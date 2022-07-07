def build_tuple(*args):
    return args


message = build_tuple("hell0", "world")
print(type(message))
print(message)

num = build_tuple(1, 2, 3)
print(type(num))
print(num)


def get_words_average_length(*args):
    return len(args)


def get_min_number(*args):
    min_num = args[0]
    for numb in args:
        if numb < min_num:
            min_num = numb
    return min_num


def get_max_number(*args):
    return max(args)


def reverse_word(*args):
    lis = []
    for word in args:
        lis.append(word[::-1])
    print(*lis, sep='\n')
    return lis


print(get_words_average_length("can", "span", "dan", "rag"))
print(get_min_number(0, 2, -10, 1, 45))
print(get_max_number(6, 2, 7, 1, 45))
print(reverse_word("Dan", "Smith", "Ken"))
