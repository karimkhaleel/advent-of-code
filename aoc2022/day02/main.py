def part1():
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


# A=rock, B=paper, C=scissors
SCORES = {"A": 1, "B": 2, "C": 3}
# what was played: (score lose, score draw, score win)
OUTCOMES = {"A": (3, 4, 8), "B": (1, 5, 9), "C": (2, 6, 7)}


def part2():
    with open("aoc2022/day02/input.txt", "r") as in_f:
        score = 0
        for line in in_f:
            match line.strip().split(" "):
                case [what_was_played, "X"]:
                    score += OUTCOMES[what_was_played][0]
                case [what_was_played, "Y"]:
                    score += OUTCOMES[what_was_played][1]
                case [what_was_played, "Z"]:
                    score += OUTCOMES[what_was_played][2]
        print(score)
