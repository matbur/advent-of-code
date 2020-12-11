#!/usr/bin/env python3

from utils.files import load_column_int

MIN = load_column_int("minimal.txt")
FULL = load_column_int("full.txt")


def foo(l, verbose=False):
    l = l[:]
    i = 0
    c = 0
    while 1:
        try:
            v = l[i]
        except IndexError:
            return c
        if verbose:
            print(
                c,
                "".join(
                    [
                        *[f" {i} " for i in l[:i]],
                        f"({l[i]})",
                        *[f" {i} " for i in l[i + 1 :]],
                    ]
                ),
            )
        l[i] += 1
        i += v
        c += 1


if __name__ == "__main__":
    print("min", foo(MIN, True))
    print("full", foo(FULL))
