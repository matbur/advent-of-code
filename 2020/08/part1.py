from pathlib import Path

data = Path("./data2.txt").read_text().splitlines()


def nop(val: int, cir: int, acc: int):
    return cir + 1, acc


def acc(val: int, cir: int, acc: int):
    return cir + 1, acc + val


def jmp(val: int, cir: int, acc: int):
    return cir + val, acc


cpu = {
    "nop": nop,
    "acc": acc,
    "jmp": jmp,
}


def parse(s: str):
    op, val = s.split()
    return op, int(val)


cir = 0
acc = 0
called = []
while True:
    op, val = parse(data[cir])
    called.append(cir)
    if len(called) != len(set(called)):
        break
    cir, acc = cpu[op](val, cir, acc)

print(acc)

if __name__ == "__main__":
    pass
