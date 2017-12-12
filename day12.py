"""
@trallard
Advent of Code 2017: Day 10
"""

import aoc
# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 12)

# Note that for this one I donwloaded the input and
# worked on the train
file = open('./inputs/17_input5.txt')
connect = {}
for line in file:
    line = line.strip().split()
    connect[line[0]] = [x.strip(',') for x in line[2:]]

seen = set()
def find_pipes(progr):
    if progr in seen:
        return
    seen.add(progr)
    for x in connect[progr]:
        find_pipes(x)


#find_pipes('0')
#print('Part 1: {}'.format(len(seen)))


seen = set()
components = 0
while len(seen) < len(connect):
    n = (set(connect.keys()) - seen).pop()
    find_pipes(n)
    components += 1
print('B', components)