from collections import namedtuple
from pathlib import Path
from typing import Tuple

data = Path("./data2.txt").read_text().splitlines()


class Pos(namedtuple("Pos", ("x", "y"), defaults=(0, 0))):
    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)


def N(pos: Pos, dir: Pos, value: int) -> Tuple[Pos, Pos]:
    pos = Pos(pos.x, pos.y + value)
    return pos, dir


def S(pos: Pos, dir: Pos, value: int) -> Tuple[Pos, Pos]:
    pos = Pos(pos.x, pos.y - value)
    return pos, dir


def E(pos: Pos, dir: Pos, value: int) -> Tuple[Pos, Pos]:
    pos = Pos(pos.x + value, pos.y)
    return pos, dir


def W(pos: Pos, dir: Pos, value: int) -> Tuple[Pos, Pos]:
    pos = Pos(pos.x - value, pos.y)
    return pos, dir


def L(pos: Pos, dir: Pos, value: int) -> Tuple[Pos, Pos]:
    if value == 90:
        dir = Pos(x=-dir.y, y=dir.x)
    elif value == 180:
        dir = Pos(x=-dir.x, y=-dir.y)
    elif value == 270:
        dir = Pos(x=dir.y, y=-dir.x)
    return pos, dir


def R(pos: Pos, dir: Pos, value: int) -> Tuple[Pos, Pos]:
    if value == 90:
        dir = Pos(x=dir.y, y=-dir.x)
    elif value == 180:
        dir = Pos(x=-dir.x, y=-dir.y)
    elif value == 270:
        dir = Pos(x=-dir.y, y=dir.x)
    return pos, dir


def F(pos: Pos, dir: Pos, value: int) -> Tuple[Pos, Pos]:
    pos = Pos(pos.x + dir.x * value, pos.y + dir.y * value)
    return pos, dir


d = {
    "N": N,
    "S": S,
    "E": E,
    "W": W,
    "L": L,
    "R": R,
    "F": F,
}

pos = Pos()
dir = Pos(x=1)
for i in data:
    action, *value = i
    value = int("".join(value))
    pos, dir = d[action](pos, dir, value)

print(pos.manhattan)

if __name__ == "__main__":
    pass
