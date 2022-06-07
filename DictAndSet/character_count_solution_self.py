# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}


def word_counting(text_to_count: str) -> dict:
    """
    Count the occurence of characters and digits in a given text
    :param text_to_count: The input test
    :return : Word count
    """
    word_to_use = ""
    for char in text_to_count:
        if char.isalnum():
            word_to_use += char.casefold()
    # Printing the dictionary
    for char in text_to_count:
        word_count[char] = word_to_use.count(char)
    return word_count

def word_counting_improved(text_to_count: str) -> dict:
    """
    Count the occurence of characters and digits in a given text
    :param text_to_count: The input test
    :return : Word count
    """
    for char in text_to_count.casefold():
        if char.isalnum():
            word_count[char] = word_count.setdefault(char, 0) + 1
    return word_count


# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

word_count = word_counting_improved(text)

for letter, count in sorted(word_count.items()):
    print(letter, count)
