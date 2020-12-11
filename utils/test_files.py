#!/usr/bin/env python3

import pytest
from string import ascii_lowercase as letters

from utils.files import (
    load_row_int,
    load_matrix_int,
    load_column_int,
    load_row,
    load_column,
    load_matrix,
)


def test_load_row_int():
    get = load_row_int("example-row-int.txt")
    want = list(range(4))
    assert get == want


def test_load_column_int():
    get = load_column_int("example-column-int.txt")
    want = list(range(4))
    assert get == want


def test_load_matrix_int():
    get = load_matrix_int("example-matrix-int.txt")
    want = [list(range(4 * i, 4 * i + 4)) for i in range(4)]
    assert get == want


def test_load_row():
    get = load_row("example-row.txt")
    want = list(letters[:4])
    assert get == want


def test_load_column():
    get = load_column("example-column.txt")
    want = list(letters[:4])
    assert get == want


def test_load_matrix():
    get = load_matrix("example-matrix.txt")
    want = [list(letters[4 * i : 4 * i + 4]) for i in range(4)]
    assert get == want


if __name__ == "__main__":
    pytest.main()
