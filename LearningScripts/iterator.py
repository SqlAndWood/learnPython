

xs = [1, 2, 3]

desc = dir(xs)
length = len(xs)
it = iter(xs)

# print(it.__sizeof__)

print(dir(it))

print(next(it))
print(next(it))
print(next(it))

# safer to loop using this
for i in it:
    print(i)


# def fib(n: int) -> Iterator[int]:
#     a, b = 0, 1
#     while a < n:
#         yield a
#         a, b = b, a+b
