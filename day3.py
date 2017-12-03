"""
@trallard
Advent of Code 2017: Day 3
"""
import aoc


# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 3)
my_input = helper.get_data()
print(my_input)

"""
First we need to create the grid for the puzzle:
Which increases as powers of odd numbers (1^2, 3^3, 5^5).
Since Aoc 2016 started using the Manhattan grid too! I decided
to follow a 'similar(ish)' approach to the way I define the
directions.. allowing me to eliminate the need to use proper
matrices (I know... I am lazy)
So we start from the example given:
"""

import numpy as np

dummy_grid = np.asarray([[ 17.,  16.,  15.,  14.,  13.],
                         [ 18.,   5.,   4.,   3.,  12.],
                         [ 19.,   6.,   1.,   2.,  11.],
                         [ 20.,   7.,   8.,   9.,  10.],
                         [ 21.,  22.,  23.,  24.,  25.]])


# Too lazy to be dealing with arrays right now so I will
# get back to this later


def offset_centre(my_input):
    # center
    x, y = 0, 0
    delta = -1 #think of this as the direction
    steps = 1
    num = 1
    while num <= my_input:
        for step in range(steps):
            x += delta
            num += 1
            if num == my_input:
                return (x,y)
        for step in range(steps):
            num += 1
            y += delta
            if num == my_input:
                return (x,y)

        delta *= -1
        steps +=1


def collect(my_input):
    x, y = offset_centre(my_input)
    return (abs(x) + abs(y))


# ---------- Testing part 1  --------
import pytest

def test_offset_centre():
    assert (collect)(12) == 3
    assert (collect)(23) == 2
    assert (collect)(1024) == 31

# Tests passed so this is now ready for submission

total = collect(int(my_input))
helper.submit(1, str(total))


# ---------- Part 2  --------
def first_larger(my_input):
    delta = -1
    steps = 1
    x, y, num= 0, 0, 1

    guide = {(0, 0): 1}
    while num <= my_input:
        for step in range(steps):
            x += delta
            guide[x, y] = sum(
                guide[dx, dy]
                for dx in range(x - 1, x + 2)
                for dy in range(y - 1, y + 2)
                if (dx, dy) in guide
            )
            if guide[x, y] >= my_input:
                return guide[x, y]
        for step in range(steps):
            y += delta
            guide[x, y] = sum(
                guide[dx, dy]
                for dx in range(x - 1, x + 2)
                for dy in range(y - 1, y + 2)
                if (dx, dy) in guide
            )
            if guide[x, y] >= my_input:
                return guide[x, y]
        delta *= -1
        steps += 1


# ---------- Testing 2  --------
def test_first_larger():
    assert (first_larger)(400) == 747
    assert (first_larger)(134) == 142


# Tests passed so this is now ready for submission

first_no = first_larger(int(my_input))
helper.submit(2, str(first_no))