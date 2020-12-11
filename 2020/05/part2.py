from pathlib import Path
from typing import Tuple


def begin(minn: int, maxx: int) -> Tuple[int, int]:
    return minn, maxx - (maxx - minn + 1) // 2


def end(minn: int, maxx: int) -> Tuple[int, int]:
    return minn + (maxx - minn + 1) // 2, maxx


d = {
    "L": begin,
    "R": end,
    "F": begin,
    "B": end,
}


def foo(s: str) -> int:
    a, b = s[:7], s[7:]

    l, r = 0, 7
    for i in b:
        l, r = d[i](l, r)

    f, b = 0, 127
    for i in a:
        f, b = d[i](f, b)

    return 8 * b + r


data = Path("./data2.txt").read_text().split()

ids = [foo(i) for i in data]
for i in ids:
    if i + 2 in ids and i + 1 not in ids:
        print(i + 1)

if __name__ == "__main__":
    pass
