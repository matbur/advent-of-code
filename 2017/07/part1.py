#!/usr/bin/env python3

from utils.files import load_matrix

MIN = load_matrix("minimal.txt")
FULL = load_matrix("full.txt")


def foo(l, verbose=False):
    d = {}
    for k, *v in l:
        d[k] = set(i.strip(",") for i in v[2:])

    s = l[-1][0]
    while True:
        for k, v in d.items():
            if s in v:
                s = k
                break
        else:
            return s


if __name__ == "__main__":
    print("min", foo(MIN, True))
    print("full", foo(FULL))
