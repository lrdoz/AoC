"""
@trallard
Advent of Code 2017: Day 7
"""
import aoc
import re


# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 7)
my_input = helper.get_data()
lines = my_input.split('\n')

def unstack(lines):
    tower = {}
    weights = {}
    seen = set()
    for line in lines:
        prog, weight, stack = re.match(r'(\w+) +\((\d+)\)(?: +-> +((?:\w+, )*\w+))?', line).groups()
        if stack:
            stack = list(map(str.strip(), stack.split()))
        else:
            stack = []
        weights[prog] = int(weight)
        tower[prog] = stack
        seen.update(stack)
        top, = tower.keys() - seen
        return top


