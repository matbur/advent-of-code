#!/usr/bin/env python3

import numpy as np

from utils.files import load_row_int

MIN = load_row_int("minimal.txt")
FULL = load_row_int("full.txt")


def foo(l, verbose=False):
    l = np.array(l)
    h = []

    n = len(l)

    if verbose:
        print(l)

    c = 0
    while l.tolist() not in h:
        h.append(l.tolist())

        am = l.argmax()
        mv = l[am]
        l[am] = 0
        for i in range(1, mv + 1):
            l[(am + i) % n] += 1
        if verbose:
            print(l)
        c += 1
    return c


if __name__ == "__main__":
    print("min", foo(MIN, True))
    print("full", foo(FULL))
