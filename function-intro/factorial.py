def factorial(num: int) -> int:
    """
    Calculate the product of all the values from 1 to the number inclusive
    Note that 0! = 1
    :param num: The input number
    :return: The product of all the numbers
    """
    k = 1
    if num == 0:
        return k
    else:
        for i in range(1, num + 1):
            k *= i
        return k


for f in range(36):
    print(f, factorial(f))


def factorial_recursion(n: int) -> int:
    """
    Return n! (0! is 1).

    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)


#for i in range(36):
#    print(i, factorial_recursion(i))
