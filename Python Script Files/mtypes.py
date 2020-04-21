#!/usr/bin/env python3
# coding:utf8

from typing import Optional
from typing import Dict


def get_first_name(full_name: str) -> str:
    if full_name == '':
        return "there"
    return full_name.split(" ")[0]


def greeting(name: Optional[str] = None) -> str:
    # this would be better than the above
    # Optional[str] means the same thing as Union[str, None]
    if name is None:
        name = 'stranger'
    return 'Hello, ' + name


fallback_name: Dict[str, str] = {
    "first_name": "UserFirstName",
    "last_name": "UserLastName"
}

raw_name: str = input("Please enter your name: ")
first_name: str = get_first_name(raw_name)

# If the user didn't type anything in, use the fallback name
if not first_name:
    first_name = get_first_name(fallback_name)

print(f"Hi, {first_name}!")


def stars(*args: int, **kwargs: float) -> None:
    # 'args' has type 'Tuple[int, ...]' (a tuple of ints)
    # 'kwargs' has type 'Dict[str, float]' (a dict of strs to floats)
    for arg in args:
        print(arg)
    for key, value in kwargs:
        print(key, value)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
