def get_integer():
    user_in = input("Enter 2 integers: ")
    try:
        print(int(user_in[0])/int(user_in[1]))
    except Exception:
        print("That was not valid")


get_integer()