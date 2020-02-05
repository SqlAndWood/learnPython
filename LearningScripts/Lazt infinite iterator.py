#!/usr/bin/env python3
# coding:utf8

from functools import partial
from itertools import accumulate, islice, repeat

# recursions


def take(n, it):
    return [x for x in islice(it, n)]


# new sequence with all but the first n values
def drop(n, it):
    return islice(it, n, None)


# force the first value of a sequence
# head = next

# # new sequence with all but the first value of a sequence
# tail = partial(drop, 1)


def add(a, b):
    return a + b


add1 = partial(add, a=1)
# if __name__ == "__main__":
#     add1 = partial(add1, a=1)
#     print("result of add1 ", add1(b=2))

# used recursion


def iterate(f, x):
    while True:
        yield x
        x = f+x  # Mutable


def lazy_integers():
    return iterate(f=add1(b=0), x=0)


rs = take(100, lazy_integers())
print(rs)
rs = take(10, lazy_integers())
print(rs)

# no recursions
print("no recursion")


def f_iterate(f, x):
    return accumulate(repeat(x), lambda fx, _: f(fx))


