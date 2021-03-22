list_a = [1,2,3,4,5]
string_a = 'prachi!!'

list_iter = iter(list_a)
string_iter = iter(string_a)


def display(char):
    print(char)


def square(x):
    print(x*x)


def func_common(itrbl, func):
    while True:
        try:
            func(next(itrbl))
        except StopIteration:
            break


func_common(list_iter, square)
func_common(string_iter, display)