# import pytest
from io import StringIO

from minemapper import write_grid


def test_write_1_by_1():
    rows = 1
    cols = 1
    grid = [['.'] * cols] * rows
    expect = """
.
""".lstrip()
    output = StringIO()
    write_grid(grid=grid, output_fh=output)
    assert output.getvalue() == expect


def test_write_2_by_2():
    rows = 2
    cols = 2
    grid = [['.'] * cols] * rows
    expect = """
..
..
""".lstrip()
    output = StringIO()
    write_grid(grid=grid, output_fh=output)
    assert output.getvalue() == expect


def test_write_1_by_20():
    rows = 1
    cols = 20
    grid = [['.'] * cols] * rows
    expect = """
....................
""".lstrip()
    output = StringIO()
    write_grid(grid=grid, output_fh=output)
    assert output.getvalue() == expect


def test_write_23_by_47():
    rows = 23
    cols = 47
    nl = '\n'
    grid = [['.'] * cols] * rows
    expect = nl.join(['.' * cols] * rows) + nl
    output = StringIO()
    write_grid(grid=grid, output_fh=output)
    assert output.getvalue() == expect


def test_write_100_by_1():
    rows = 100
    cols = 1
    nl = '\n'
    grid = [['.'] * cols] * rows
    expect = nl.join(['.' * cols] * rows) + nl
    output = StringIO()
    write_grid(grid=grid, output_fh=output)
    assert output.getvalue() == expect


def test_write_1_by_100():
    rows = 1
    cols = 100
    nl = '\n'
    grid = [['.'] * cols] * rows
    expect = nl.join(['.' * cols] * rows) + nl
    output = StringIO()
    write_grid(grid=grid, output_fh=output)
    assert output.getvalue() == expect


def test_write_100_by_100():
    rows = 100
    cols = 100
    nl = '\n'
    grid = [['.'] * cols] * rows
    expect = nl.join(['.' * cols] * rows) + nl
    output = StringIO()
    write_grid(grid=grid, output_fh=output)
    assert output.getvalue() == expect

# END
