"""
@trallard
Advent of Code 2017: Day 9
"""
import aoc
import collections
import re

# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 9)
my_input = helper.get_data()

print(my_input)


# rules to remember groups: {}, garbage: <>
# ignore anything after !

def stream_cleaner(stream, part):
    garbage = False
    groups = 0
    prev_group = 0
    garb_total = 0

    i = 0

    stream = iter(stream)
    for char in stream:
        if garbage == True:
            if char == '>':
                garbage = False
            elif char == '!':
                next(stream)
            else:
                garb_total += 1
        else:
            if char == '{':
                prev_group += 1
                groups += prev_group
            elif char == '}':
                prev_group += -1
            elif char == '<':
                garbage = True
    if part ==1 :
        return groups
    else:
        return garb_total

#---- Testing part 1 and 2
import pytest
def test_stream_cleaner():
    assert(stream_cleaner)('{}',1) ==1
    assert (stream_cleaner)('{{{}}}', 1) == 6
    assert (stream_cleaner)('{{{},{},{{}}}}', 1) == 16
    assert (stream_cleaner)('{{<ab>},{<ab>},{<ab>},{<ab>}}', 1) == 9
    assert (stream_cleaner)('{{<!!>},{<!!>},{<!!>},{<!!>}}', 1)==9
    assert (stream_cleaner)('<>', 2) == 0
    assert (stream_cleaner)('<random characters>', 2) == 17
    assert (stream_cleaner)('<{o"i!a,<{i<a>', 2) == 10

# Tests passed now to submit
part1 = stream_cleaner(my_input)
helper.submit(1, str(part1))

part2 = stream_cleaner(my_input, 2)
helper.submit(2, str(part2))