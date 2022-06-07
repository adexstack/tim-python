def sum_numbers(*values: float) -> float:
    """
    Calculate the sum of all numbers passed as arguments
    :param values: The numbers to be added ....
    :return: The sum of all the input numbers
    """
    # longer solution
    # j = 0
    # for i in values:
    #     j += i
    # return j

    # smarter using builtin
    return sum(values)



print(sum_numbers(-1, 2.5, 3))
