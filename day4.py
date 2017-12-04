"""
@trallard
Advent of Code 2017: Day 4
"""
import aoc
import collections


# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 4)
my_input = helper.get_data()
lines = my_input.split('\n')


#------- Part 1 --------
def get_valid():
    valid = 0
    for line in lines:
        word  = line.split()
        if len(word) == len(set(word)):
            valid += 1
    return(valid)


valid = get_valid()
helper.submit(1, str(valid))

#------- Part 2 --------
def anagrams():
    total = 0
    for line in lines:
        word = line.split()
        an = [tuple(sorted(collections.Counter(x).items())) for x in word]
        if len(set(an)) == len(word):
            total += 1
    return(total)


valid = anagrams()
helper.submit(2, str(valid))