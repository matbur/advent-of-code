#!/usr/bin/env python3

from part1 import MIN, FULL


def bar(l):
    return sum([len(set([''.join(sorted(j)) for j in i])) == len([''.join(sorted(j)) for j in i]) for i in l])


if __name__ == '__main__':
    print('min', bar(MIN))
    print('full', bar(FULL))
