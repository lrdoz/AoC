"""
@trallard
Advent of Code 2017: Day 6
"""
import aoc

# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 6)
my_input = helper.get_data()
mem_blocks = tuple(int(x) for x in my_input.split())

# print(mem_blocks)


def debug_mem(blocks, part):
    seen = {}
    mutable = list(blocks)
    while blocks not in seen:
        seen[blocks] = len(seen)
        ln = len(mutable)
        i, elem = max(enumerate(mutable), key=lambda x: x[1])
        mutable[i] = 0
        while elem:
            i = (i + 1) % ln
            mutable[i] += 1
            elem -= 1
        blocks = tuple(mutable)
    if part == 1:
        return len(seen)
    elif part == 2:
        return (len(seen) - seen[blocks])


# ---------- Testing  --------
import pytest

def test_debug_mem():
    assert (debug_mem)((0,2,7,0),1) == 5
    assert (debug_mem)((0,2,7,0),2) == 4



# ---------- Tests passed so can submit  --------
part1 = debug_mem(mem_blocks, 1)
#helper.submit(1, str(part1))


part2 = debug_mem(mem_blocks, 2)
#helper.submit(2, str(part2))
