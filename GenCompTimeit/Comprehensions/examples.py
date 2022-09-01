text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

# don't unnecessarily us elist comprehension else you evaluating the gotten list
lc_words = text.split(' ')
print(lc_words)