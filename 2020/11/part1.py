from pathlib import Path
from typing import List

data = Path("./data2.txt").read_text().splitlines()
data = [list(i) for i in data]

empty = "L"
occupied = "#"
floor = "."


def get_adjacent(l: List[List[str]], row: int, col: int):
    for r in (-1, 0, 1):
        for c in (-1, 0, 1):
            if r == c == 0:
                continue
            rr = row + r
            cc = col + c
            if 0 <= rr < len(l) and 0 <= cc < len(l[0]):
                yield rr, cc


def step(l: List[List[str]]) -> List[List[str]]:
    new = [[j for j in i] for i in l]
    for row in range(len(l)):
        for col in range(len(l[0])):
            if l[row][col] == floor:
                continue

            if l[row][col] == empty and all(
                l[r][c] != occupied for r, c in get_adjacent(l, row, col)
            ):
                new[row][col] = occupied
                continue

            if (
                l[row][col] == occupied
                and [l[r][c] for r, c in get_adjacent(l, row, col)].count(occupied) >= 4
            ):
                new[row][col] = empty
                continue

    return new


while True:
    tmp = step(data)
    if tmp == data:
        break
    data = tmp

print([i for j in data for i in j].count(occupied))

if __name__ == "__main__":
    pass
