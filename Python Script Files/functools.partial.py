#!/usr/bin/env python3
# coding:utf8
from functools import partial
# functools.partial
# from functools import reduce
import re

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010'), basetwo.__doc__)


def doubleIt(x, y): return x * y


dblIt = partial(doubleIt, x=2)
dblIt.__doc__ = 'im a good dev'
print(dblIt(y=9), dblIt.__doc__)


def adder(x, y): return x + y


assert adder(x=1, y=1) == 2
assert adder(x=5, y=5) == 10
assert adder(x=6, y=2) == 8

add_five = partial(adder, y=5)
# #now it adds 5!
# # x=1, y=5
# assert add_five(x=1) == 6
# print(add_five(x=1))


def add(a, b):
    return a + b


def add2number(x, y, z):
    return x + y + z


if __name__ == "__main__":
    a = partial(add, a=2)
    print("result of add2 ", a(b=2))
    vader3 = partial(partial(add2number, y=1), z=12)
    print("result of add3", vader3(x=1))


# def is_grouped_together(text):
#     return re.search('[a-zA-Z]\=', text)
# search(pattern, string, flags=0)
is_grouped_together = partial(re.search, pattern='[a-zA-Z]\\=', flags=0)

# def is_spaced_apart(text):
#     return re.search('[a-zA-Z]\s\=', text)
is_spaced_apart = partial(re.search, pattern='[a-zA-Z]\\s\\=', flags=0)

# def and_so_on(text):
#     return re.search("pattern_188364625", text)


# 'https://chriskiehl.com/article/the-great-white-space-debate'

lines = ('for (int i=0; i<LENGTH; i++)',
         'for (int i = 0; i < LENGTH; i++)',
         'for(int i=0;i<LENGTH;i++)')

# if is_grouped_together(string='for (int i=0; i<LENGTH; i++)'):
#     print('g')

grouped_together_count = 0
spaced_apart_count = 0
other_count = 0
for text in lines:
    if is_grouped_together(string=text):
        # print('grouped', text)
        grouped_together_count += 1

    elif is_spaced_apart(string=text):
        # print('spaced', text)
        spaced_apart_count += 1

    else:
        # print('other', text)
        other_count += 1

print(grouped_together_count, spaced_apart_count, other_count)
