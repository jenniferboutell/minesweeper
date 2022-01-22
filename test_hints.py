# import pytest

from minemapper import add_grid_hints_one


def test_validate_hints_producing_function_1_mine():
    grid = [['.', '.', '.'],
            ['.', '*', '.'],
            ['.', '.', '.']]
    add_grid_hints_one(grid)
    assert grid == [[1, 1, 1],
                    [1, '*', 1],
                    [1, 1, 1]] 


def test_validate_hints_producing_function_0_mine():
    grid = [['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]
    add_grid_hints_one(grid)
    assert grid == [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]


def test_validate_hints_producing_function_all_mines():
    grid = [['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '*']]
    add_grid_hints_one(grid)
    assert grid == [['*', '*', '*'],
                    ['*', '*', '*'],
                    ['*', '*', '*']]


def test_validate_hints_producing_function_8_mines():
    grid = [['*', '*', '*'],
            ['*', '.', '*'],
            ['*', '*', '*']]
    add_grid_hints_one(grid)
    assert grid == [['*', '*', '*'],
                    ['*', 8, '*'],
                    ['*', '*', '*']]


def test_validate_hints_producing_function_3_mines_diagonal():
    grid = [['*', '.', '.'],
            ['.', '*', '.'],
            ['.', '.', '*']]
    add_grid_hints_one(grid)
    assert grid == [['*', 2, 1],
                    [2, '*', 2],
                    [1, 2, '*']]


def test_validate_hints_producing_function_8_mines_mixed():
    grid = [['*', '.', '.', '.'],
            ['*', '.', '.', '*'],
            ['.', '*', '*', '*'],
            ['.', '*', '.', '*']]
    add_grid_hints_one(grid)
    assert grid == [['*', 2, 1, 1],
                    ['*', 4, 4, '*'],
                    [3, '*', '*', '*'],
                    [2, '*', 5, '*']]

# END
