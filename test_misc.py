from io import StringIO

from minemapper import xlate_grids


def test_validate_program_1_field():
    test_infile = StringIO(initial_value="""
2 2
..
..
0 0
""")
    output = StringIO
    expected_outfile = """
Field #1:
00
00
""".lstrip()
    xlate_grids(test_infile, output)
    assert output == expected_outfile


def test_validate_program_0_field():
    test_infile = StringIO(initial_value='0 0')
    output = StringIO
    expected_outfile = ''.lstrip()
    xlate_grids(test_infile, output)
    assert output == expected_outfile


def test_validate_program_3_fields():
    test_infile = StringIO(initial_value="""
1 2
..
2 3
.*.
*..
3 5
*...*
..*..
.....
0 0
""")
    output = StringIO
    expected_outfile = """
Field #1:
00

Field #2:
2*1
*20

Field #3:
*212*
12*21
01110
""".lstrip()
    xlate_grids(test_infile, output)
    assert output == expected_outfile


def test_validate_program_entire_input_file():
    with open('minesweeper_input.txt', 'r') as infile, open('minesweeper_output.txt') as outfile, \
    open('minesweeper_valid_output.txt') as expected_outfile:
        xlate_grids(infile, outfile)
        assert outfile == expected_outfile