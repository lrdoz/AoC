"""
@trallard
Advent of Code 2017: Day 10
"""

connect = {}
for line in open('./inputs/17_input5.txt'):
    line = line.strip().split()
    connect[line[0]] = [x.strip(',') for x in line[2:]]


seen = set()
def find_pipes(progr):
    if progr in seen:
        return
    seen.add(progr)
    for x in connect[progr]:
        find_pipes(x)


find_pipes('0')
print(seen)
print(len(seen))