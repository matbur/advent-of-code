#!/usr/bin/env python3

import pytest

from utils.files import load_row, load_matrix, load_column


def test_load_row():
    get = load_row('example-row.txt')
    want = list(range(4))
    assert get == want


def test_load_column():
    get = load_column('example-column.txt')
    want = list(range(4))
    assert get == want


def test_load_matrix():
    get = load_matrix('example-matrix.txt')
    want = [list(range(4 * i, 4 * i + 4)) for i in range(4)]
    assert get == want


if __name__ == '__main__':
    pytest.main()
