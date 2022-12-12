from collections import deque


def part1():
    with open("aoc2022/day06/input.txt", "r") as in_f:
        d = deque(maxlen=4)
        line = in_f.readline()
        for i, c in enumerate(line):
            d.append(c)
            if len(set(d)) == 4:
                print(i + 1)
                break


def part2():
    with open("aoc2022/day06/input.txt", "r") as in_f:
        d = deque(maxlen=14)
        line = in_f.readline()
        for i, c in enumerate(line):
            d.append(c)
            if len(set(d)) == 14:
                print(i + 1)
                break


part1()
