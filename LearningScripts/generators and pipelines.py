#!/usr/bin/env python3
# coding:utf8

# cat eular.hs | grep -i -prime | wc -i
# http://www.dba-oracle.com/op_unix_16_cat_grep_commands.htm
# word count command

from itertools import tee


# the long way


with open("functional\gp.txt", "r") as f:
    lines = (line for line in f)
    prime_lines = filter(lambda line: "easter" in line.lower(), lines)
    line_count = len(list(prime_lines))

print(line_count)


# the better way?
