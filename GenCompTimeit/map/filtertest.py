menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]


def meal_for():
    meal_list = []
    for meal in menu:
        if "spam" not in meal:
            meal_list.append(meal)
    return meal_list


def meal_comp():
    return [meal for meal in menu if "spam" not in meal]
    #return [meal for meal in menu if not_spam(meal)] # using not_spam function if the filtering is complex (slower tho)


def not_spam(meal_list: list):
    return "spam" not in meal_list


def spam_filter():
    return list(filter(not_spam, menu))


if __name__ == "__main__":
    import timeit

    print(meal_for())
    print('-' * 30)
    print(meal_comp())
    print('-' * 30)
    print(spam_filter())
    print(timeit.timeit(meal_for, number=10000))
    print(timeit.timeit(meal_comp, number=10000))
    # Using filter is lot less slower than list comprehension because of the using from another function
    print(timeit.timeit(spam_filter, number=10000))

