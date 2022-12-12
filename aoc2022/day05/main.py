import re

configuration = [
    ["F", "L", "M", "W"],
    ["F", "M", "V", "Z", "B"],
    ["Q", "L", "S", "R", "V", "H"],
    ["J", "T", "M", "P", "Q", "V", "S", "F"],
    ["W", "S", "L"],
    ["W", "J", "R", "M", "P", "V", "F"],
    ["F", "R", "N", "P", "C", "Q", "J"],
    ["B", "R", "W", "Z", "S", "P", "H", "V"],
    ["W", "Z", "H", "G", "C", "J", "M", "B"],
]

for l in configuration:
    l.reverse()


def part1():
    with open("aoc2022/day05/input.txt", "r") as in_f:
        for line in in_f:
            c, f, t = map(int, re.findall(r"(\d+)", line))
            for _ in range(c):
                configuration[t - 1].append(configuration[f - 1].pop())
    res = ""
    for stack in configuration:
        res += stack.pop()
    print(res)


def split(l, i):
    len_l = len(l)
    diff = len_l - i
    return l[:diff], l[diff:]


def part2():
    with open("aoc2022/day05/input.txt", "r") as in_f:
        for line in in_f:
            c, f, t = map(int, re.findall(r"(\d+)", line))
            f1, f2 = split(configuration[f - 1], c)
            configuration[f - 1] = f1
            configuration[t - 1].extend(f2)
    res = ""
    for stack in configuration:
        res += stack.pop()
    print(res)


part2()
