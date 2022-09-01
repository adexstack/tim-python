import sys

def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1

big_range =  my_range(1000)
#big_range =  range(1000)
print(f"range bytes is {sys.getsizeof(big_range)}")

big_list = list(big_range)
print(f"list bytes is {sys.getsizeof(big_list)}")