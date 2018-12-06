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


##############################################################################
# Part 1
##############################################################################


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


##############################################################################
# Part 2
##############################################################################


def part2(data):
    hasher = set()
    for line in data:
        for i, _ in enumerate(line):
            key = (line[:i], line[i + 1 :])
            if key in hasher:
                return key[0] + key[1]
            hasher.add(key)


def p2_alt(data):
    combos = combinations(input, 2)
    for combo in combos:
        if sum(map(lambda x, y: x != y, combo[0], combo[1])) == 1:
            return "".join([x for x, y in zip(combo[0], combo[1]) if x == y])


print(part1(x))
print(part2(x))


# ---- All the tests -------
p1_test_input = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

p2_test_input = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]


def test_part1():
    assert part1(p1_test_input) == 12


def test_part2():
    assert part2(p2_test_input) == "fgij"
