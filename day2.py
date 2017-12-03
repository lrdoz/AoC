"""
@trallard
Advent of Code 2017: Day 2
"""

import itertools

import aoc

# Getting the input for the puzzle
helper = aoc.Data(year = 2017, day = 2)
my_input = helper.get_data()
rows = data.split('\n')

with open('./inputs/17_2input.txt') as code:
    rows= code.read().strip().split('\n')

# Getting at it
def checksum1():
    check = 0
    for row in rows:
        nums = list(map(int, row.split()))
        check+= max(nums) - min(nums)
    return check

def checksum2():
    check = 0
    for row in rows:
        nums = list(map(int, row.split()))
        for x, y in itertools.combinations(nums, 2):
            print(x, y)
            if (x % y) == 0 or (y % x) == 0:
                check += x//y or y//x
    return check

# Note: This was my first attempt at part 2
# it work correctly but I kinda prefer the
#itertools approach

def check2_long():
    check = 0
    for row in rows:
        nums = list(map(int, row.split()))
        for x in nums:
            for y in nums:
                if (x % y) == 0 and x != y:
                    check += x//y
    return check

print('Part 1: {}'.format(checksum1()))
print('Part 2: {}'.format(checksum2()))
print('Part 2: {}'.format(check2_long()))

#---- Automatic submission -------
helper.submit(1, str(checksum()))
helper.submit(2, str(checksum2()))