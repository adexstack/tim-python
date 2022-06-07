text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}
print(prepositions)

# Add your code here.
words = set(text.split())
preps_used = prepositions.intersection(words)
print(preps_used)

# preps_used = set(words) & prepositions
# print(preps_used)