from palindrome import user_palindrome_check

sentence = input("Please enter a sentence to check\n")


def is_palindrome():
    alpha_numeric = ""
    for char in sentence:
        if char.isalnum():
            alpha_numeric += char
    user_palindrome_check(alpha_numeric)


is_palindrome() # #radar , Do geese see god?
