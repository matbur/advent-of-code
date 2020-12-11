from pathlib import Path

data = Path('./data3.txt').read_text().splitlines()
data = [int(i) for i in data]
data += [0, max(data) + 3]
data = sorted(data)

l = [data[i] - v for i, v in enumerate(data[:-1], 1)]

print(l.count(3) * l.count(1))

if __name__ == '__main__':
    pass
