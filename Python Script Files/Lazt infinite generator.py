#!/usr/bin/env python3
# coding:utf8


def lazy_integer(n=0):
    while True:
        yield n
        n += 1   # Mutable


xs = lazy_integer()

print([next(xs) for _ in range(10)])
print([next(xs) for _ in range(10)])

print([next(xs) for _ in range(50)])
print([next(xs) for _ in range(6)])

squares = (s**2 for s in lazy_integer())

print(next(squares))
print(next(squares))
print(next(squares))  # ie, infinite number available
# infinite loop = bad
# squares = [x**2 for x in lazy_integer() ]

doubles = (d*2 for d in lazy_integer())
print(next(doubles))
print(next(doubles))
