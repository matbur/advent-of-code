import re
from pathlib import Path
from pprint import pprint
from typing import Tuple, List


def parse(s: str):
    key, contains = re.findall(r'(\w+ \w+) bags contain (.*)', s)[0]
    if contains == 'no other bags.':
        return key, []
    l = []
    for i in contains.split(', '):
        quantity, color = re.findall(r'(\d+) (\w+ \w+)', i)[0]
        l.append([color, int(quantity)])
    return key, l


sg = 'shiny gold'


def get_paths(d: List):
    q = [(d, [])]
    while q:
        n, p = q.pop(0)
        if p:
            yield p
        if isinstance(n, list):
            for i, v in enumerate(n):
                q.append((v, p + [i]))  # Change to q.append((v, p)) to remove index


data = Path('./data1.txt').read_text().splitlines()

d = dict([parse(i) for i in data])
pprint(d)


def find_path(l: List, f):
    for path in get_paths(l):
        value = l
        for j in path:
            value = value[j]
        if f(value):
            return path


def replace_with_value(l: List):
    while path := find_path(l, lambda x: isinstance(x, str)):
        value = l
        parent = value
        for j in path:
            parent = value
            value = value[j]
        if d[value]:
            parent[j] = d[value]
        else:
            del parent[j]


def bar(l: List):
    while path := find_path(l, lambda x: isinstance(x, list) and len(x) == 1):
        value = l
        parent = value
        for j in path:
            parent = value
            value = value[j]
        parent[j] = value[0]


def bar2(l: List):
    while path := find_path(l, lambda x: isinstance(x, list) and all(isinstance(i, int) for i in x) and len(x) == 2):
        value = l
        parent = value
        for j in path:
            parent = value
            value = value[j]
        parent[j] = sum(value)


q = d[sg]
replace_with_value(q)
pprint(q)
bar(q)
pprint(q)
bar2(q)
pprint(q)

if __name__ == '__main__':
    pass
