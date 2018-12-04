"""
@trallard
Advent of Code 2017: Day 14
Permuation promenade
"""
import aoc

# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 16)
my_input = helper.get_data()

print(my_input)

def dance(p, input):
    moves = my_input.split(',')
    for m in moves:
        if m[0] == 's':
            n = int(m[1:])
            p = p[-n:] + p[:-n]
        elif m[0] == 'x':
            n, m = map(int, m[1:].split('/'))
            p[n], p[m] = p[m], p[n]
        elif m[0] == 'p':
            n, m = p.index(m[1]), p.index(m[-1])
            p[n], p[m] = p[m], p[n]
    return p

def part1(input):
    return ''.join(dance(list('abcdefghijklmnop'), input))

print(part1(my_input))

def long_dance(p, input):
    seen = {}
    target = 1000000000

    moves = my_input.split(',')
    for i in range(target):
        x = ''.join(p)
        if x in seen:
            cycle_size = i - seen[x]
            break
        seen[x] = i
        p = dance(p, moves)

    target = (target - i) % cycle_size
    for i in range(target):
        p = dance(p, moves)
    return ''.join(p)

def part2(input):
    return ''.join(long_dance(list('abcdefghijklmnop'), input))

print(part2(my_input))
