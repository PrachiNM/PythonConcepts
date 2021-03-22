import time

class Generator:
    def fib_gen(self, num):
        a = 0
        b = 1
        count = 0
        while count < num:
            a, b = b, a+b
            yield a
            count += 1


if __name__ == '__main__':
    # obj = Generator()
    # # c = obj.counter(10)
    # for x in obj.fib_gen(10):
    #     print(x**2)
    start = time.time()
    sumx = sum([x for x in range(1000000000)])
    print(sumx)
    print(time.time()-start)

    start = time.time()
    sumx = sum(x for x in range(1000000000))
    print(sumx)
    print(time.time() - start)

