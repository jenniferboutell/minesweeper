# import pytest
from io import StringIO

from minemapper import read_grid_spec


def test_read_1_by_1():
    test_infile = StringIO(initial_value="""1 1
.
""")
    grid = read_grid_spec(test_infile)
    assert len(grid) == 1 and len(grid[0]) == 1


def test_read_2_by_2():
    test_infile = StringIO(initial_value="""2 2
..
..
""")
    grid = read_grid_spec(test_infile)
    assert len(grid) == 2 and len(grid[0]) == 2


def test_read_1_by_20():
    test_infile = StringIO(initial_value="""1 20
.....*...*.....*...*
""")
    grid = read_grid_spec(test_infile)
    assert len(grid) == 1 and len(grid[0]) == 20


def test_read_23_by_47():
    rows = 23
    cols = 47
    nl = '\n'
    test_infile = StringIO(initial_value=f"""{rows} {cols}
{ nl.join(['.' * cols] * rows) }
""")
    grid = read_grid_spec(test_infile)
    assert len(grid) == rows and len(grid[0]) == cols


def test_read_100_by_1():
    rows = 100
    cols = 1
    nl = '\n'
    test_infile = StringIO(initial_value=f"""{rows} {cols}
{ nl.join(['.' * cols] * rows) }
""")
    grid = read_grid_spec(test_infile)
    assert len(grid) == rows and len(grid[0]) == cols


def test_read_1_by_100():
    rows = 1
    cols = 100
    nl = '\n'
    test_infile = StringIO(initial_value=f"""{rows} {cols}
{ nl.join(['.' * cols] * rows) }
""")
    grid = read_grid_spec(test_infile)
    assert len(grid) == rows and len(grid[0]) == cols


def test_read_100_by_100():
    rows = 100
    cols = 100
    nl = '\n'
    test_infile = StringIO(initial_value=f"""{rows} {cols}
{ nl.join(['.' * cols] * rows) }
""")
    grid = read_grid_spec(test_infile)
    assert len(grid) == rows and len(grid[0]) == cols

# END
