import timeit

text = "what have the romans ever done for us"


def comp_capitals():
    capitals = [char.upper() for char in text]
    return capitals


# use map
def map_capitals():
    capitals = list(map(str.upper, text))
    return capitals



def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words


# use map
def map_words():
    words = list(map(str.upper, text.split(' ')))
    return words


if __name__ == "__main__":
    print(comp_capitals())
    print(map_capitals())
    print(comp_words())
    print(map_words())

    #print(timeit.timeit(comp_capitals, number=10000))
    # difference between up and below is above is simplicity, no output difference between bot:
    print(timeit.timeit("comp_capitals()", setup="from map_intro import comp_capitals", number=10000))
    print(timeit.timeit("map_capitals()", setup="from map_intro import map_capitals", number=10000))
    print(timeit.timeit("comp_words()", setup="from map_intro import comp_words", number=10000))
    print(timeit.timeit("map_capitals()", setup="from map_intro import map_capitals", number=10000))

# 0.026947599999402883
# 0.022443699999712408
# 0.009546500001306413
# 0.021737800001574215