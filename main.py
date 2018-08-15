""" Simple recursive definition of fibonacci, used for debugging quiz. """


def fib(i):
    """ Return the nth fibonacci number, starting with 1. """
    if i < 1:
        raise Exception("Cannot commute fibonacci when n < 1")
    elif i <= 2:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


def fibs(i):
    """ Return a list of the first n fibonacci numbers. """
    import ipdb; ipdb.set_trace()
    return [fib(x) for x in range(1, i + 1)]


if __name__ == "__main__":
    print fibs(20)
