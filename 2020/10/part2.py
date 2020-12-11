from pathlib import Path
from typing import List

data = Path("./data1.txt").read_text().splitlines()
data = [int(i) for i in data]
data += [0, max(data) + 3]
data = sorted(data)


def foo(l: List):
    diffs = [l[i] - v for i, v in enumerate(l[:-1], 1)]
    return diffs  #


def is_valid(l: List) -> bool:
    diffs = [l[i] - v for i, v in enumerate(l[:-1], 1)]
    valid = (1, 2, 3)
    return min(diffs) in valid and max(diffs) in valid


def bar(l: List) -> List:
    l_ = []
    for i in range(1, len(l) - 1):
        if l[i + 1] - l[i - 1] > 3:
            continue
        l_.append(l[i])
    return l_


def split(l: List):
    n = 0
    for i in range(1, len(l) - 1):
        if l[i + 1] - l[i - 1] <= 3:
            continue
        yield l[n : i - 1]
        n = i - 1
    pass


cache = set()


def fuzzer(l: List) -> int:
    n = 0
    bar1 = bar(l)
    for i in bar1:
        l2 = tuple(l[:i] + l[i + 1 :])
        cache.add(l2)
        n += 1 + fuzzer(l2)
    return n


for i in split(data):
    print(i)
print()
# print(fuzzer(data))
# print(foo(data))
print(bar(data))
print(data)
#
# print(len(cache))

if __name__ == "__main__":
    pass
