# A=rock, B=paper, C=scissors
SCORES = {"A": 1, "B": 2, "C": 3}
# what was played: (score lose, score draw, score win)
OUTCOMES = {"A": (3, 4, 8), "B": (1, 5, 9), "C": (2, 6, 7)}


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
