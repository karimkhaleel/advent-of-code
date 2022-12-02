with open("aoc2022/day02/input.txt", "r") as in_f:
    score = 0
    for line in in_f:
        match line.strip().split(" "):
            case ["A", "X"]:
                score += 4
            case ["A", "Y"]:
                score += 8
            case ["A", "Z"]:
                score += 3
            case ["B", "X"]:
                score += 1
            case ["B", "Y"]:
                score += 5
            case ["B", "Z"]:
                score += 9
            case ["C", "X"]:
                score += 7
            case ["C", "Y"]:
                score += 2
            case ["C", "Z"]:
                score += 6
    print(score)
