"""
@trallard
Advent of Code 2018
title: "Day 1: Chronal Calibration"
"""
import collections
import pytest
import re
import aoc


# Getting the input for the puzzle
helper = aoc.puzzle_data(year=2018, day=3)
data = helper.get_data().strip().split("\n")  # so that we have a list of numbers


def matchy_match(expression):
    regex_match = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", expression)
    claim_id, left, top, width, height = map(int, regex_match.groups())
    return claim_id, left, top, width, height


def trim_areas(data):
    all_claims = collections.defaultdict(int)
    for claim in data:
        claim_id, left, top, width, height = matchy_match(claim)
        for x in range(left, left + width):
            for y in range(top, top + height):
                all_claims[x, y] += 1
    return sum(1 for count in all_claims.values() if count > 1)


print(trim_areas(data))


data_ns = helper.get_data().strip()  # so that we have a list of numbers


def both_alt(input):
    fabric_size = 1000
    fabric = [list() for _ in range(fabric_size ** 2)]

    p = re.compile(r"#(\d*) @ (\d*),(\d*): (\d*)x(\d*)")
    matches = re.findall(p, input)

    for match in matches:
        claim_id, x, y, w, h = map(int, match)
        for i in range(h):
            curr_pos = ((y + i) * fabric_size) + x
            for pos in range(curr_pos, curr_pos + w):
                fabric[pos].append(claim_id)

    p1 = len([len(square) for square in fabric if len(square) >= 2])

    all_claim_ids = set([int(match[0]) for match in matches])

    for square in fabric:
        if len(square) > 1:
            all_claim_ids = all_claim_ids - set(square)

    p2 = list(all_claim_ids)[0]
    return p1, p2


alt = both_alt(data_ns)  # alternate solution
