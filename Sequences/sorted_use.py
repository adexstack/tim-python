# .sort sorts in place
# sorted creates a new object

pangram = "The quick brown fox jumps over the lazy dog"
letters = set(sorted(pangram.replace(" ", "").casefold()))
print(sorted(list(letters)))

# using keyword argument to ignore case
missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letter)

names = ["Erin", "joe", "Kan", "dave"]
names.sort(key=str.casefold)
print(names)

