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

# ---- Part 1 -----
def unstack(lines, part = 1):
    tower = {} #dictionary to collect the various subtowers
    weights = {} #weights of the programs
    seen = set() #will help to match the elements to subtowers
    for line in lines:
        prog, weight, elements = re.match(r"(\w+) +\((\d+)\)(?: +-> +((?:\w+, )*\w+))?", line).groups()
        if elements:
            elements = list(map(str.strip, elements.split(',')))
        else:
            elements = []
        weights[prog] = int(weight)
        tower[prog] = elements
        seen.update(elements)
    top, = tower.keys() - seen
    print('*******')
    if part == 1:
        return(top)
    else:
        req(top, tower, weights)


part1 = unstack(lines)
#helper.submit(1, str(part1))

def req(top, tower, nums):
    elements = tower[top]
    vs = [(element, req(element, tower, nums)) for element in elements]
    multiple = 0
    seen = set()
    for elem, v in vs:
        if v in seen:
            multiple = v
        seen.add(v)
    seen.discard(multiple)
    if seen:
        value, = seen
        odd = next(elem for elem, v in vs if v == value)
        print(nums[odd] - (value - multiple))
    return nums[top] + len(vs) * multiple

#part2 = unstack(lines, 2)
#print(part2)



