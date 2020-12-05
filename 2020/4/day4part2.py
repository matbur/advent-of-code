from pathlib import Path


def byr(s: str) -> bool:
    if not s.isdigit(): return False
    return 1920 <= int(s) <= 2002


def iyr(s: str) -> bool:
    if not s.isdigit(): return False
    return 2010 <= int(s) <= 2020


def eyr(s: str) -> bool:
    if not s.isdigit(): return False
    return 2020 <= int(s) <= 2030


def hgt(s: str) -> bool:
    if s.endswith('cm'):
        s = s[:-2]
        if not s.isdigit(): return False
        return 150 <= int(s) <= 193
    if s.endswith('in'):
        s = s[:-2]
        if not s.isdigit(): return False
        return 59 <= int(s) <= 76
    return False


def hcl(s: str) -> bool:
    if len(s) != 7: return False
    if not s.startswith('#'): return False
    s = s[1:]
    try:
        int(s, 16)
    except ValueError:
        return False
    else:
        return True


def ecl(s: str) -> bool:
    return s in 'amb blu brn gry grn hzl oth'.split()


def pid(s: str) -> bool:
    return len(s) == 9 and s.isdigit()


fields = {'byr': byr, 'ecl': ecl, 'eyr': eyr, 'hcl': hcl, 'hgt': hgt, 'iyr': iyr, 'pid': pid}
names = set(fields.keys())

data = Path('./data2.txt').read_text().split('\n\n')


def foo(passport):
    names2 = {i.split(':')[0] for i in passport}
    if len(names - names2) != 0:
        return False

    d = [i.split(':') for i in passport]
    for k, v in d:
        if k == 'cid':
            continue
        if not fields[k](v):
            return False
    return True


a = [foo(i.split()) for i in data]
print(sum(a))

if __name__ == '__main__':
    pass
