"""
@trallard
Advent of Code 2017: Day 8
"""
import aoc
import collections
import re

# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 8)
my_input = helper.get_data().split('\n')

#print(my_input)

def reg_hell(lines, part):
    regs = collections.Counter()
    maxx = 0
    for line in lines:
        reg, decl, val, base, cond, differ = re.match(r"(\w+) (inc|dec) (-?\d+) if (\w+) (\S+) (\S+)", line).groups()
        if eval(f'{regs[base]} {cond} {differ}'):
            val = int(val)
            if decl == 'dec':
                val *= -1
            regs[reg] += val
            maxx = max(maxx, regs[reg])
    if part == 1:
        return (max(regs.values()))  # part 1
    else:
        return maxx  # part 2


part1 = reg_hell(my_input,1)
helper.submit(1, str(part1))


part2 = reg_hell(my_input,2)
helper.submit(2, str(part2))