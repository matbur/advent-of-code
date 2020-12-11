#!/usr/bin/env python3
from pprint import pprint

from part1 import MIN, FULL, foo


def bar2(l, verbose=False):
    d = {}
    for k, *v in l:
        d[k] = [eval(v[0]), set(i.strip(",") for i in v[2:])]
        d[k].append(d[k][0])

    f = foo(l)
    while True:
        for k, v in d.items():
            if not v[1] and k != f:
                break
        s = k
        for k, v in d.items():
            if s in v[1]:
                s = k
                break
        s_ = [d[i][0] for i in d[s][1]]
        if not all_equal(s_):
            dd = list(d[s][1])
            idx, t = find_outsider([d[i][0] for i in dd])
            if t == "ma":
                return d[dd[idx]][2] - (d[dd[idx]][0] - d[dd[(idx + 1) % len(dd)]][0])
            return d[dd[idx]][2] + (d[dd[(idx + 1) % len(dd)]][0] - d[dd[idx]][0])
        for i in d[s][1]:
            if not d[i][1]:
                del d[i]
        d[s] = [d[s][0] + sum(s_), set(), d[s][0]]


def bar(l, verbose=False):
    d = {}
    for k, *v in l:
        d[k] = [i.strip(",") for i in v[2:]]

    # f = foo(l)
    for i in d:
        if not d[i][1]:
            break
    if verbose:
        pprint(d)
        print(i)

    print(d[i][1][:])
    for i, v in enumerate(d[i][1][:]):
        print(i)
        s = d.pop(v)
        print(s)
        d[i][1][i] = s

    pprint(d)


def all_equal(l):
    if not l:
        return True
    s = l[0]
    for i in l:
        if i != s:
            return False
    return True


def find_outsider(l):
    mi = min(l)
    if l.count(mi) == 1:
        return l.index(mi), "mi"
    ma = max(l)
    if l.count(ma) == 1:
        return l.index(ma), "ma"
    raise ValueError


if __name__ == "__main__":
    print("min", bar(MIN, True))
    # print('full', bar(FULL))
