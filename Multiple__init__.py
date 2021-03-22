# considers only the latest method definition
# when multiple methods with same name are defined.
# thus, method overloading is not supported implicitly by python

class A:

    def __init__(self):
        print("from no arg __init__")

    def __init__(self):
        print("from argd __init__")

    def square(self):
        print('from square 1')

    def square(self, num):
        print('from square 2')


if __name__ == '__main__':
    a = A()
    a.square()




