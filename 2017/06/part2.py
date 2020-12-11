#!/usr/bin/env python3

import numpy as np

from part1 import MIN, FULL


def bar(l, verbose=False):
    l = np.array(l)
    h = {}

    n = len(l)

    if verbose:
        print(l)

    c = 0
    while tuple(l) not in h:
        h[tuple(l)] = c

        am = l.argmax()
        mv = l[am]
        l[am] = 0
        for i in range(1, mv + 1):
            l[(am + i) % n] += 1
        if verbose:
            print(l)
        c += 1
    return c - h[tuple(l)]


if __name__ == "__main__":
    print("min", bar(MIN, True))
    print("full", bar(FULL))
