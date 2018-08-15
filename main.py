""" Simple recursive definition of fibonacci, used for debugging quiz. """


def fib(i):
    """ Return the ith fibonacci number, starting with 1. """
    if i < 1:
        raise Exception("Cannot commute fibonacci when n < 1")
    elif i <= 2:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


def fibs(x):
    """ Return a list of the first x fibonacci numbers. """
    return [fib(y) for y in range(1, x + 1)]


if __name__ == "__main__":
    print fibs(8)
