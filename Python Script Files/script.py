# python -m venv myvirtenv

import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(a):
   # te = "te"
    greeting = 'hi, {}'.format(a)
    return greeting


print(greet("Andrew"))

r = requests.get('https://coreyms.com')
print(r.status_code)




