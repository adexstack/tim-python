# using generators with yield
def genNum():
    start = 0
    while True:
        yield start
        start += 1


num = genNum()

for i in range(11):
    print(next(num))

