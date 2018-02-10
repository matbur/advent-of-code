#!/usr/bin/env python3

from part1 import MIN, FULL


def bar(l, verbose=False):
    l = l[:]
    i = 0
    c = 0
    while 1:
        try:
            v = l[i]
        except IndexError:
            return c
        if verbose:
            print(c, ''.join([*[f' {i} ' for i in l[:i]], f'({l[i]})', *[f' {i} ' for i in l[i + 1:]]]))
        l[i] += 1 if v < 3 else -1
        i += v
        c += 1


if __name__ == '__main__':
    print('min', bar(MIN, True))
    print('full', bar(FULL))
