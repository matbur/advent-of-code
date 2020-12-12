from collections import namedtuple
from pathlib import Path
from typing import Tuple

data = Path("./data2.txt").read_text().splitlines()


class Pos(namedtuple("Pos", ("x", "y"), defaults=(0, 0))):
    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)


def N(pos: Pos, wp: Pos, value: int) -> Tuple[Pos, Pos]:
    wp = Pos(wp.x, wp.y + value)
    return pos, wp


def S(pos: Pos, wp: Pos, value: int) -> Tuple[Pos, Pos]:
    wp = Pos(wp.x, wp.y - value)
    return pos, wp


def E(pos: Pos, wp: Pos, value: int) -> Tuple[Pos, Pos]:
    wp = Pos(wp.x + value, wp.y)
    return pos, wp


def W(pos: Pos, wp: Pos, value: int) -> Tuple[Pos, Pos]:
    wp = Pos(wp.x - value, wp.y)
    return pos, wp


def L(pos: Pos, wp: Pos, value: int) -> Tuple[Pos, Pos]:
    if value == 90:
        wp = Pos(x=-wp.y, y=wp.x)
    elif value == 180:
        wp = Pos(x=-wp.x, y=-wp.y)
    elif value == 270:
        wp = Pos(x=wp.y, y=-wp.x)
    return pos, wp


def R(pos: Pos, wp: Pos, value: int) -> Tuple[Pos, Pos]:
    if value == 90:
        wp = Pos(x=wp.y, y=-wp.x)
    elif value == 180:
        wp = Pos(x=-wp.x, y=-wp.y)
    elif value == 270:
        wp = Pos(x=-wp.y, y=wp.x)
    return pos, wp


def F(pos: Pos, wp: Pos, value: int) -> Tuple[Pos, Pos]:
    pos = Pos(pos.x + wp.x * value, pos.y + wp.y * value)
    return pos, wp


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
wp = Pos(10, 1)
for i in data:
    action, *value = i
    value = int("".join(value))
    pos, wp = d[action](pos, wp, value)

print(pos.manhattan)

if __name__ == "__main__":
    pass
