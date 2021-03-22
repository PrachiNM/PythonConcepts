def fun_args(*args):
    for a in args:
        print(a, end=' ')
    print()


def fun_kwargs(elem, **kwargs):
    a = kwargs
    print(elem)
    for key in kwargs:
        print(key, end=" ")


fun_args(1, 2, 3, 4, 5)
fun_kwargs('sequence elements', a=1, b=2, c=3)
