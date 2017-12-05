"""
@trallard
Advent of Code 2017: Day 5
"""
import aoc
import collections


# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 5)
my_input = helper.get_data().split('\n')
offsets = [int(offset) for offset in my_input]
print(offsets)

# ----- Part 1 -----

def trampoline(offset):
    i = 0
    jump = 0
    while 0 <= i < len(offset):
        offset[i] += 1
        jump +=1
        i += offset[i] - 1

    return jump

# ----- Test part 1 -----
import pytest

def test_trampoline():
    assert (trampoline)([0, 3, 0, 1, -3]) == 5


# ----- Test passed so this can be submitted

part1 = trampoline(offsets)
helper.submit(1, str(part1))


# ----- Part 2 -----
def trampoline_2(offset):
    i = 0
    jump = 0
    while 0 <= i < len(offset):
        jump +=1
        new = -1 if offset[i] >= 3 else 1
        offset[i] += new
        i += offset[i] - new
    print(offset)
    return jump

# ----- Test part 2 -----
import pytest

def test_trampoline_2():
    assert (trampoline_2)([0, 3, 0, 1, -3]) == 10

# ----- Test passed so this can be submitted

part2 = trampoline_2(offsets)
helper.submit(2, str(part2))
