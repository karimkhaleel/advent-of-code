from functools import reduce


def part1():
    with open("aoc2022/day03/input.txt", "r") as in_f:
        total = 0
        for line in in_f:
            line.strip()
            half = len(line) // 2
            c = ord(set(line[:half]).intersection(set(line[half:])).pop())
            if c < 97:
                total += c - 38
            else:
                total += c - 96
        print(total)


def part2():
    with open("aoc2022/day03/input.txt", "r") as in_f:
        total = 0
        lines = []
        for line in in_f:
            line = line.strip()
            lines.append(set(line))
            if len(lines) == 3:
                c = ord(reduce(lambda x, y: x.intersection(y), lines).pop())
                if c < 97:
                    total += c - 38
                else:
                    total += c - 96
                lines.clear()
        print(total)
