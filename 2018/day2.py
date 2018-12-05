"""
@trallard
Advent of Code 2018
title: "Day 2: Inventory Management System"
"""
import collections
import pytest
import aoc

# Getting the input for the puzzle
helper = aoc.puzzle_data(year=2018, day=2)
x = helper.get_data().strip().split("\n")


def part1(data):
    twos = 0
    threes = 0
    for line in data:
        c = collections.Counter(line)
        has_two = False
        has_three = False
        for k, v in c.items():
            if v == 2:
                has_two = True
            if v == 3:
                has_three = True
        twos += has_two
        threes += has_three
    return twos * threes


def part2(data):
    hasher = set()
    for line in data:
        for i, _ in enumerate(line):
            key = (line[:i], line[i+1:])
            if key in hasher:
                return key[0] + key[1]
            hasher.add(key)

print(part1(x))
print(part2(x))
