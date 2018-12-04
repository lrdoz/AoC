"""
@trallard
Advent of Code 2018
title: "Day 1: Chronal Calibration"
"""
import pytest
import aoc

# Getting the input for the puzzle
helper = aoc.puzzle_data(year=2018, day=1)
x = helper.get_data().strip().split()  # so that we have a list of numbers
freq = list(map(int, x))

##############################################################################
# Part 1
##############################################################################
def freq1(freq):
    return sum(freq)


print(f"Part 1: {freq1()}")

##############################################################################
# Part 2
##############################################################################
def freq_repeat(freq):
    uniques = set()
    count = 0
    while True:
        for f in freq:
            count += f
            if count in uniques:
                return count
            uniques.add(count)


print(f"Part 2:{freq_repeat(freq)}")


# ---- All the tests -------


def test_freq1():
    assert freq1([1, -2, 3, 1]) == 3
    assert freq1([1, 1, 1]) == 3
    assert freq1([1, 1, -2]) == 0


def test_freq_repeat():
    assert freq_repeat([1, -1]) == 0
    assert freq_repeat([3, 3, 4, -2, -4]) == 10


# # ---- Automatic submission -------
helper.submit(1, str(freq1(freq)))
helper.submit(2, str(freq_repeat(freq)))
