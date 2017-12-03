"""
@trallard
Advent of Code 2017: Day 1
"""

import aoc

# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 1)
x = helper.get_data()

def captcha1():
    return sum(map(int,[ x[i] for i in range(len(x)) if x[i] == x[i - 1] ]))

def captcha2():
    return sum(int(x[i]) for i in range(len(x)) if x[i] == x[i - len(x) // 2])


print('Part 1: {}'.format(captcha1()))
print('Part 2: {}'.format(captcha2()))


#---- Automatic submission -------
helper.submit(1, str(captcha1()))
helper.submit(2, str(captcha2()))