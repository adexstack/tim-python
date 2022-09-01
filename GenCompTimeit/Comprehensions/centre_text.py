def centre_text(*args):
    text = ""
    for arg in args:
        text += str(arg) + "-"
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)
 
 
# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")
 
centre_text("first", "second", 3, 4, "spam")

# Using list comprehension for an improved handling
def centre_text2(*args):
    text = ""
    text = " ".join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text2("spam and eggs")
centre_text2("spam, spam and eggs")
centre_text2(12)
centre_text2("spam, spam, spam and spam")

centre_text2("first", "second", 3, 4, "spam")