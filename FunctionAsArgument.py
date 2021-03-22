def add(*args):
    total = 0
    for elem in args:
        total += elem
    return total


def sub(*args):
    args = list(args)
    diff = args.pop(0)
    for elem in args:
        diff -= elem
    return diff


def fun_call(func, *args):
    return func(*args)


if __name__ == '__main__':
    print(fun_call(add, 1, 2, 3, 4, 5))
    print(fun_call(sub, 7, 3, 2))
