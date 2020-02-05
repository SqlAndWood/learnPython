# coding:utf8

from __future__ import division, print_function
import sys
from pprint import pprint


# import modules
import random
import datetime


# class UserProperty:
#     def __init__(self, v0, v1, v2, v3, v4):
#         self.greg = v0
#         self.sarah = v1
#         self.barry = v2
#         self.rachel = v3
#         self.tim = v4

#     def __repr__(self):
#         return 'UserProperty(%r,%r,%r,%r,%r )'\
#             % (self.greg, self.sarah, self.barry, self.rachel, self.tim)


# colors = UserProperty('blue',  'orange', 'green', 'yellow', 'red')
# cities = UserProperty('austin', 'dallas', 'tuscon', 'reno', 'portland')
# fruit = UserProperty('apple',  'banana', 'orange', 'pear', 'peach')


# for p in [colors, cities, fruit]:
#     print(vars(p))

# thanks to mark shannon for the underlying python code since 3.5
# print(list(map(sys.getsizeof, map(vars, [colors, cities, fruit]))))

# linear search
keys = "greg sarah barry rachel tim".split()
v1 = 'blue orange green yellow red'.split()
v2 = 'austin dallas tuscon reno portland'.split()
v3 = 'apple banana orange pear peach'.split()
v4 = 'a b c d e'.split()

v5 = {'Jan 2 2012', 'Jan 16 2015', 'Feb 2 2000', 'Feb 3 1998',  'aug 3 1975'}


print(v5)
hashes = list(map(abs, map(hash, keys)))
entries = list(zip(hashes, keys, v1))
comb_entries = list(zip(hashes, keys, v1, v2, v3, v4, v5))
# print(len(keys))
# print(hashes)
# print(entries)
# print(comb_entries)
# print('>')


# not efficient
# def db_linear_search():
#     pprint(list(zip(keys, v1, v2, v3)))


# db_linear_search()

# chaining

# def sep_chaining(n):
#     buckets = [[] for i in range(n)]

#     for pair in entries:
#         h, _, _ = pair
#         # print(pair)
#         i = h % n
#         buckets[i].append(pair)
#     print(buckets)


# sep_chaining(2)
# print('>')
# sep_chaining(4)
# print('>')
# sep_chaining(8)
# print('>')
# 4312979683708570856

# # castrophic linear pile up
# def open_addressing_linear(n):
#     table = [None] * n
#     for h, key, value in entries:
#         i = h % n
#         while table[i] is not None:
#             i = (i+1) % n
#         table[i] = (key, value)
#     print(table)


# open_addressing_linear(8)

# not a good idea either!
# def open_addressing_multihashing(n):

#     if n < len(keys):
#         n = len(keys)*4

#     print('%r attempts' % n)

#     table = [None] * n
#     for h, key, value in entries:
#         perterbed = h
#         i = h % n
#         while table[i] is not None:
#             print('%r collided with %r' % (key, table[i][0]))
#             #i = (i+1) % n
#             i = (5 * i + perterbed + 1) % n
#             perterbed >> 5
#         table[i] = (key, value)
#     print(table)


# open_addressing_multihashing(8)

# def compact_and_ordered():

#     n = len(keys) * 2

#     print('%r attempts' % n)

#     table = [None] * n

#     for pos, entry in enumerate(entries):
#         h = perterbed = entry[0]
#         i = h % n
#         while table[i] is not None:
#             print('%r collided with %r' % (pos, entry))
#             #i = (i+1) % n
#             i = (5 * i + perterbed + 1) % n
#             perterbed >> 5
#         table[i] = pos
#     print(table)
#     pprint(entries)
    # pprint(table)


# compact_and_ordered()

def share_and_compact():
    'compact, ordered and shared'
    n = len(keys) * 4

    table = [None] * n

    for pos, entry in enumerate(comb_entries):
        h = perterbed = entry[0]
        i = h % n
        while table[i] is not None:
            # print('%r collided with %r' % (comb_entries[pos], entry))
            i = (5 * i + perterbed + 1) % n
            perterbed >> 5
        table[i] = pos
    print(table)
    pprint(comb_entries)
  
share_and_compact()

