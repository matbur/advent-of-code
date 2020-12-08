from pathlib import Path
from typing import List

data = Path('./data2.txt').read_text().splitlines()


def nop(val: int, cir: int, acc: int):
    return cir + 1, acc


def acc(val: int, cir: int, acc: int):
    return cir + 1, acc + val


def jmp(val: int, cir: int, acc: int):
    return cir + val, acc


cpu = {
    'nop': nop,
    'acc': acc,
    'jmp': jmp,
}


def parse(s: str):
    op, val = s.split()
    return op, int(val)


def run(data: List[str]):
    cir = 0
    acc = 0
    called = []
    while True:
        op, val = parse(data[cir])
        called.append(cir)
        if len(called) != len(set(called)):
            break
        cir, acc = cpu[op](val, cir, acc)
        if cir == len(data):
            return acc


def fuzzer(data: List[str]):
    fuzz = {
        'jmp': 'nop',
        'nop': 'jmp',
    }
    for i, v in enumerate(data):
        data_copy = data[:]
        if v.startswith(('jmp', 'nop')):
            op, val = parse(v)
            if val == 0:
                continue
            data_copy[i] = f'{fuzz[op]} {val}'
            yield data_copy


for i in fuzzer(data):
    print(i)
    acc = run(i)
    if acc is not None:
        print(acc)
        break

if __name__ == '__main__':
    pass
