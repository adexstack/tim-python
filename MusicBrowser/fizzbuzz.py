def fizzbuzz(num):
    try:
        if num > 0:
            if num % 15 == 0:
                print('fizzbuzz')
            elif num % 5 == 0:
                print('fizz')
            elif num % 3 == 0:
                print('buzz')
            else:
                pass
        else:
            print("Number must be greater than 0")
    except TypeError:
        print("That is not a number")


fizzbuzz(45)
