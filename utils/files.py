#!/usr/bin/env python3

from pathlib import Path


def load_row_int(fn):
    s = Path(fn).read_text().split()
    i = [int(i) for i in s]
    return i


def load_column_int(fn):
    s = Path(fn).read_text().splitlines()
    i = [int(i) for i in s]
    return i


def load_matrix_int(fn):
    s = Path(fn).read_text().splitlines()
    i = [[int(j) for j in i.split()] for i in s]
    return i


def load_row(fn):
    s = Path(fn).read_text().split()
    return s


def load_column(fn):
    s = Path(fn).read_text().splitlines()
    return s


def load_matrix(fn):
    s = Path(fn).read_text().splitlines()
    i = [i.split() for i in s]
    return i
