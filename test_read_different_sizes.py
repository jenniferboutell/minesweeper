from minemapper import read_grid_spec


def test_read_1_by_1():
    with open('test_temp.txt', 'w') as test_outfile:
        sample = "1 1\n."
        test_outfile.write(sample)
    with open('test_temp.txt', 'r') as test_infile:
        grid = read_grid_spec(test_infile)
    assert len(grid) == 1 and len(grid[0]) == 1


def test_read_2_by_2():
    with open('test_temp.txt', 'w') as test_outfile:
        sample = "2 2\n" \
                 "..\n" \
                 ".."
        test_outfile.write(sample)
    with open('test_temp.txt', 'r') as test_infile:
        grid = read_grid_spec(test_infile)
    assert len(grid) == 2 and len(grid[0]) == 2


def test_read_1_by_20():
    with open('test_temp.txt', 'w') as test_outfile:
        sample = "1 20\n" \
                 ".....*...*.....*...*"
        test_outfile.write(sample)
    with open('test_temp.txt', 'r') as test_infile:
        grid = read_grid_spec(test_infile)
    assert len(grid) == 1 and len(grid[0]) == 20


def test_read_23_by_47():
    with open('test_temp.txt', 'w') as test_outfile:
        sample = "23 47\n" \
                 # insert generated output here
        test_outfile.write(sample)
    with open('test_temp.txt', 'r') as test_infile:
        grid = read_grid_spec(test_infile)
    assert len(grid) == 23 and len(grid[0]) == 47


def test_read_100_by_1():
    with open('test_temp.txt', 'w') as test_outfile:
        sample = "100 1\n" \
                 # insert generated output here
        test_outfile.write(sample)
    with open('test_temp.txt', 'r') as test_infile:
        grid = read_grid_spec(test_infile)
    assert len(grid) == 100 and len(grid[0]) == 1


def test_read_1_by_100():
    with open('test_temp.txt', 'w') as test_outfile:
        sample = "1 100\n" \
                 # insert generated output here
        test_outfile.write(sample)
    with open('test_temp.txt', 'r') as test_infile:
        grid = read_grid_spec(test_infile)
    assert len(grid) == 1 and len(grid[0]) == 100


def test_read_100_by_100():
    with open('test_temp.txt', 'w') as test_outfile:
        sample = "100 100\n" \
                 # insert generated output here
        test_outfile.write(sample)
    with open('test_temp.txt', 'r') as test_infile:
        grid = read_grid_spec(test_infile)
    assert len(grid) == 100 and len(grid[0]) == 100

