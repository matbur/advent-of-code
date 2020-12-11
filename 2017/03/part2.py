#!/usr/bin/env python3

import numpy as np

from part1 import foo


def bar(n):
    m = [
        np.array([1, 0]),
        np.array([1, 1]),
        np.array([0, 1]),
        np.array([-1, 1]),
        np.array([-1, 0]),
        np.array([-1, -1]),
        np.array([0, -1]),
        np.array([1, -1]),
    ]
    l = {(0, 0): 1}
    for i in range(2, n + 2):
        j = np.array(foo(i))
        s = 0
        for k in m:
            s += l.get(tuple(k + j), 0)
        l[tuple(j)] = s
        if s > n:
            return s


if __name__ == "__main__":
    print("min")
    for i in range(20):
        print(i, bar(i))

    print("full", bar(265149))
