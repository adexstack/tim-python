def ispalindrome(word):
    reverse = ""
    for letters in range(len(word) - 1, -1, -1):
        reverse += word[letters]
    print(reverse)
    if word == reverse:
        print("It is palindrome")
    else:
        print("not palindrome")


ispalindrome("rahul")


# optimised reverse string for palindrome check
def is_palindrome_word(string):
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word or sentence to check")


def user_palindrome_check(word):
    if is_palindrome_word(word):
        print(f"'{word}' is a palindrome") #radar , Do geese see god?
    else:
        print(f"'{word}' is not a palindrome") # python


user_palindrome_check(word)