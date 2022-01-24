from io import StringIO

from minemapper import xlate_grids


def test_xlate_1_field():
    test_infile = StringIO(initial_value="""
2 2
..
..
0 0
""".lstrip())
    output = StringIO()
    expected_output = """
Field #1:
00
00

""".lstrip()
    xlate_grids(test_infile, output)
    assert output.getvalue() == expected_output


def test_xlate_0_field():
    test_infile = StringIO(initial_value='0 0\n')
    output = StringIO()
    expected_output = ''
    xlate_grids(test_infile, output)
    assert output.getvalue() == expected_output


def test_xlate_3_fields():
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
""".lstrip())
    output = StringIO()
    expected_output = """
Field #1:
00

Field #2:
2*1
*21

Field #3:
*212*
12*21
01110

""".lstrip()
    xlate_grids(test_infile, output)
    assert output.getvalue() == expected_output


def _test_xlate_files(infile_name: str, outfile_name: str):
    with open(infile_name, 'r') as infile, StringIO() as output, \
            open(outfile_name, 'r') as expected_outfile:
        xlate_grids(infile, output)
        assert output.getvalue() == expected_outfile.read()


def test_xlate_official():
    _test_xlate_files(infile_name='official_input.txt', outfile_name='official_output.txt')


def test_xlate_generated():
    _test_xlate_files(infile_name='minesweeper_input.txt', outfile_name='minesweeper_output.txt')

# END
