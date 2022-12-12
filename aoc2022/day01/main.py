import heapq


def part1():
    with open("aoc2022/day01/input.txt", "r") as in_f:
        max_cals = 0
        running_total = 0
        for line in in_f:
            line = line.strip()
            if not line:
                max_cals = max(running_total, max_cals)
                running_total = 0
                continue
            running_total += int(line)
        print(max_cals)


with open("aoc2022/day01/input.txt", "r") as in_f:
    totals = []
    running_total = 0
    for line in in_f:
        line = line.strip()
        if not line:
            totals.append(running_total)
            running_total = 0
            continue
        running_total += int(line)
    print(sum(heapq.nlargest(3, totals)))
