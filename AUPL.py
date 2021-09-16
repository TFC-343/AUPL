"""Ariel's useful python library.

a bunch of usefull vars and function
that would be useful on a code-to-code basis
"""

import random
import time
from dataclasses import dataclass

__author__ = "TFC343"

__version__ = "1.1.1.4"  # <major>.<minor>.<patch>.<build>


one_hundred_and_thirty_seven = 137  # efficient method of accesing number: 137


def sarc_text(text):
    """makes text sarcastic"""
    text = list(text)
    for i in rlen(text):
        if i % 2:
            text[i] = text[i].upper()
    text = ''.join(text)
    return text


def rlen(list_):
    """becouse range(len(foo)) is far too much effort"""
    return range(len(list_))

def roll_dice(roll: str) -> int:
    """rolls dice using dice notation"""
    roll = roll.split('d')
    total = 0
    for _ in range(int(roll[0])):
        total += random.randint(1, int(roll[1]))
    return total

def prod(list_):
    """multiplies all data in a list or list-type object"""

    t = 1
    for i in list_:
        t *= i
    return t


@dataclass
class multiplier:
    """used to multiply number by multiplier
    then convert to int without too much nesting"""
    factor: float  # the factor of multiplication
    round: bool = True  # will we round the result to an int?

    def __mul__(self, other):
        if self.round:
            return round(self.factor * other)
        return self.factor * other

    def __rmul__(self, other):
        if self.round:
            return round(self.factor * other)
        return self.factor * other


class record(object):
    """simple c struct like data set"""
    def __init__(self, **data):
        self.data = data

    def __repr__(self):
        return str(self.data)

    def __getattr__(self, item):
        return self.data[item]

    def __setattr__(self, key, value):
        super(record, self).__setattr__(key, value)

    def __delattr__(self, item):
        self.data.pop(item)

    def __or__(self, other):
        """merging records"""
        return record(**(self.data | other.data))


class timer:
    """for timing how long a code takes to exacute"""
    def start_timer(self):
        """run at start of program"""
        self.time_ = time.time()

    def get_time(self):
        """use at end to program to return time took to exacute"""
        return time.time() - self.time_

timer = timer()

## -----------------------------------------------------
## -------------------- test module --------------------

if __name__ == '__main__':
    timer.start_timer()
    MULT = multiplier(0.5)
    print(15 * MULT)
    a = ['a', 'b', 'c', 'd', 'e']
    for i in rlen(a):
        print(a[i])
    rectagle = record(width=5, length=3)
    print(f"width: {rectagle.width}")
    print(repr(MULT))
    print(f"result of 2d6: {roll_dice('2d6')}")
    time.sleep(0.2)

    print(sarc_text('yeah, of course you did'))

    print(timer.get_time())
