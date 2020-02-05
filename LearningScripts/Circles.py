
#!/usr/bin/env python3
# coding:utf8
class Circle:

    def __init__(self, diameter):
        self.diameter = diameter

    @property
    def radius(self):
        'Half of the diameter'          # <== docstring
        return self.diameter / 2.0


var = Circle(diameter=9)

rad = var.radius

print(rad)
