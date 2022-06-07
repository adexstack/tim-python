menu = ("""Please choose your option from the list below:
1. Learn Python
2. Learn Java
3. Go swimming
4. Have dinner
5. Go to bed
0. Exit
""")

choice = "-"
while choice != "0":
    if choice in "12345":
        print(f"Good, you typed {choice}")
    else:
        print(menu)
    choice = input("please choose between 1 and 5 or 0 to exit\n")
else:
    print("Exiting the loop")

