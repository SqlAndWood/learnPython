#!/usr/bin/env python3
# coding:utf8

from itertools import islice
from functools import partial

# force first n values of a sequence


def take(n, it):
    return [x for x in islice(it, n)]


# new sequence with all but the first n values
def drop(n, it):
    return islice(it, n, None)


# force the first value of a sequence
head = next

# new sequence with all but the first value of a sequence
tail = partial(drop, 1)


