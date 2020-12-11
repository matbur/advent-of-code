#!/usr/bin/env python3

from utils.files import load_matrix

MIN = load_matrix("minimal.txt")
FULL = load_matrix("full.txt")


def foo(l):
    return sum([len(set(i)) == len(i) for i in l])


if __name__ == "__main__":
    print("min", foo(MIN))
    print("full", foo(FULL))
