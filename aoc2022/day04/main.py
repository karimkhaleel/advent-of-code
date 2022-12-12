def part1():
    with open("aoc2022/day04/input.txt", "r") as in_f:
        cnt = 0
        for line in in_f:
            r1, r2 = line.strip().split(",")
            r11, r12 = map(int, r1.split("-"))
            r21, r22 = map(int, r2.split("-"))
            s1 = set(range(r11, r12 + 1))
            s2 = set(range(r21, r22 + 1))
            if s1.issuperset(s2) or s2.issuperset(s1):
                cnt += 1
    print(cnt)


def part2():
    with open("aoc2022/day04/input.txt", "r") as in_f:
        cnt = 0
        for line in in_f:
            r1, r2 = line.strip().split(",")
            r11, r12 = map(int, r1.split("-"))
            r21, r22 = map(int, r2.split("-"))
            s1 = set(range(r11, r12 + 1))
            s2 = set(range(r21, r22 + 1))
            if s1.intersection(s2):
                cnt += 1
    print(cnt)


part2()
