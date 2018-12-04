"""
@trallard
Advent of Code 2017: Day 11
"""
import aoc

# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 11)
my_input = helper.get_data()
print(my_input)

def distance(x, y, z):
    return sum(map(abs, [x, y, z])) // 2


def main(file):
    x, y, z = 0, 0, 0
    d = 0
    for line in file:
        if line == 'ne':
            x += 1
            z -= 1
        elif line == 'sw':
            x -= 1
            z += 1
        elif line == 's':
            y -= 1
            z += 1
        elif line == 'n':
            y += 1
            z -= 1
        elif line == 'nw':
            x -= 1
            y += 1
        elif line == 'se':
            x += 1
            y -= 1
        else:
            raise Exception("can't got there!)
        d = max(d, distance(x, y, z))
    print(distance(x, y, z))
    print(d)

main(my_input.split(','))
