def func(p1, p2, *args, k, **kwargs):
    print(f"positional or keyword are... {p1} {p2}")
    print(f"var positional arguments...{args}")
    print(f"keyword:....................{k}")
    print(f"var keyword arguments are....{kwargs}")
    print(f"{args[1]}")


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)
