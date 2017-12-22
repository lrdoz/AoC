"""
@trallard
Advent of Code 2017: Day 14
Dueling generators
"""
import aoc

# Getting the input for the puzzle
helper = aoc.puzzle_data(year = 2017, day = 15)
my_input = helper.get_data()


print(my_input)

div = 2147483647
a = 277
b = 349

def generate(a, b, div):
    A = 16807
    B = 48271
    count = 0
    mask = (1 << 16) -1
    for i in range(40000000):
        a = (a* A) % div
        b = (b * B) % div
        if (a & mask) == (b & mask):
            count += 1
    return count


def generate2(a, b, div):
    count = 0
    mask = (1 << 16) - 1
    A = 16807
    B = 48271
    for i in range(5000000):
        a = (a * A) % 2147483647
        while a % 4 != 0:
            a = (a * A) % 2147483647
        b = (b * B) % 2147483647
        while b % 8 != 0:
            b = (b * B) % 2147483647
        if (a & mask) == (b & mask):
            count += 1
    return (count)

print(generate2(a, b, div))