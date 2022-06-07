import json

# json limitation
# json format does not support tuples. Hence, serializing this would give us lost
languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]

# Serializing data to json
with open('test.json', 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)

# deserializing it back to python object
with open('test.json') as testfile:
    data = json.load(testfile)
print(data)
print(data[2])