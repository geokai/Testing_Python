"""Calculate.py - simple calculator program"""

# This file was created on 17/09/2017
# Author: George Kaimakis - https://github.com/geokai


class Calculate(object):
    """calculator class"""

    def __init__(self):
        """empty initializer"""

    def add(self, x, y):
        """add calculator method - return x + y. Test for type int"""
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError('Invalid type: {} and {}'.format(type(x), type(y)))


if __name__ == '__main__':
    calc = Calculate()
    result = calc.add(2, 2)
    print(result)
