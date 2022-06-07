# fibonacci Self
def calc_fibonacci(sequence):
    """Return the 'n' th Fibonacci number, for positive 'n' ."""
    fib = [0, 1]
    if 0 <= sequence <= 1:
        fib = sequence
    elif sequence < 0:
        fib = None
    for num in range(sequence - 2):
        last_item = fib[-1]
        second_to_last = fib[-2]
        fib.append(last_item + second_to_last)
    print(fib)


calc_fibonacci(5)

# fibonacci Tim
def fibonacciTim(n):
    if 0 < n <= 1:
        return n
    n_minus2, n_minus1 = 0, 1

    result = None
    for i in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


fibonacciTim(5)




