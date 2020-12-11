#!/usr/bin/env python3


def foo(N):
    d = [0, 0, 0, 0]
    s = 1
    for i in range(2, N + 1):
        n = i // 2
        d_i = (i - 2) % 4
        sn = s + n
        if sn == N:
            d[d_i] += n
            break
        elif sn < N:
            d[d_i] += n
            s += n
        else:
            d[d_i] += N - s
            break
    return d[0] - d[2], d[1] - d[3]


def foo2(n):
    x, y = foo(n)
    return abs(x) + abs(y)


if __name__ == "__main__":
    print("min")
    for i in (1, 12, 23, 1024):
        print(i, foo2(i))

    print("full", foo2(265149))
