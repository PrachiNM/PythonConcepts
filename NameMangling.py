class NameMangling:

    def __init__(self):
        self.a = 'a'
        self.__b = 'c'

    def _meth1(self):
        print("from _meth1")

    def __meth2(self):
        print("from __meth2")


if __name__ == '__main__':
    n = NameMangling()
    print(n.a)
    print(n._NameMangling__b)
    n._meth1()
    n._NameMangling__meth2()
    print(n.__b)
