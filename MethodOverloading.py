# method overloading is not implicitly supported by python
# it can be achieved by using dispatch decorator from multipledispatch library
# use @dispatch(<type>, <type>, ...) before method definition

from multipledispatch import dispatch


class MethodOverloading:
    @dispatch(int, int)
    def __init__(self, a, b):
        print('from __init__ with 2 args')

    @dispatch()
    def __init__(self):
        print('from __init__ with no args')

    @dispatch(str, str)
    def add(self, str1, str2):
        return str1+str2

    @dispatch(int, int)
    def add(self, int1, int2):
        return int1+int2


if __name__ == '__main__':
    a = MethodOverloading()
    b = MethodOverloading(1,2)

    print(a.add(4,5))
    print(b.add('hiii ', 'python'))
