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
