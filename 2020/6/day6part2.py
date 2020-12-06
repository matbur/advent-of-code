from pathlib import Path


def count(s: str) -> int:
    values = set([i for i in s if i != '\n'])
    votes = [set(i) for i in s.split()]
    for i in votes:
        values = values.intersection(i)
    return len(values)


data = Path('./data2.txt').read_text().split('\n\n')

print(sum([count(i) for i in data]))

if __name__ == '__main__':
    pass
