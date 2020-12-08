import re
from pathlib import Path
from typing import Tuple, List, Dict


def parse(s: str) -> Tuple[str, Dict[str, Dict]]:
    key, contains = re.findall(r'(\w+ \w+) bags contain (.*)', s)[0]
    if contains == 'no other bags.':
        return key, {}
    d = {}
    for i in contains.split(', '):
        color = re.findall(r'(?:\d+) (\w+ \w+)', i)[0]
        d[color] = {}
    return key, d


def foo(d: dict):
    s = set()
    for k, c in d.items():
        for k2 in c:
            c[k2] = d[k2]
    return s


def get_paths(d: dict):
    q = [(d, [])]
    while q:
        n, p = q.pop(0)
        yield p
        if isinstance(n, dict):
            for k, v in n.items():
                q.append((v, p + [k]))


def trim_lists(l: List):
    try:
        return l[:l.index('shiny gold')]
    except ValueError:
        return []


data = Path('./data2.txt').read_text().splitlines()

d = dict([parse(i) for i in data])

foo(d)
lists = [trim_lists(i) for i in get_paths(d)]
print(len(set([i for j in lists for i in j])))

if __name__ == '__main__':
    pass
