from itertools import combinations
from pathlib import Path

preable, data = Path('./data2.txt').read_text().split('\n\n')
preable = int(preable)
data = [int(i) for i in data.splitlines()]

for i, v in enumerate(data[preable:], preable):
    previous = data[i - preable:i]
    for c in combinations(previous, 2):
        if sum(c) == v:
            break
    else:
        break

for i, _ in enumerate(data):
    for j in range(i + 2, len(data)):
        sliced = data[slice(i, j)]
        if sum(sliced) == v:
            print(min(sliced) + max(sliced))

if __name__ == '__main__':
    pass
