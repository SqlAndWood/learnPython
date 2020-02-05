#!/usr/bin/env python3
# coding:utf8
"""
Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.

    reduce() is defined in “functools” module, accumulate() in “itertools” module.
    reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a list containing the intermediate results. The last number of the list returned is summation value of the list.
    reduce(fun,seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.
"""

import operator
from functools import reduce


lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))


# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(reduce(operator.add, ["geeks", " ", "for", " ", "geeks"]))
# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(reduce(operator.concat, ["geeks", " ", "for", " ", "geeks"]))
