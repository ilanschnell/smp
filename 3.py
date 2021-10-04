def foo(x):
    match x:
        case float():
            print(f"got a float: {x=}")
        case x if x < 0:
            print(f"x is negative: {x=}")
        case _:
            print(f"default: {x=}")

foo(-3.0)
foo(-3)
foo(0)
