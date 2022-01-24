#!/usr/bin/env python
# TCSS504 - 2022 Winter - warmup/readiness assignment
# Consume a series of grid-maps a la Minesweeper, showing locations of mines,
# and emit corresponding series of grid-maps that populated unmined cells
# with hints, ie count (0-8) of mines in adjacent cells.

from typing import Optional, Union, TextIO
from io import StringIO

TextHandle = Union[TextIO, StringIO]

"""
Default input and output files.
"""
g_dflt_infile = 'input.txt'
g_dflt_outfile = 'output.txt'


def read_dimens(input_fh: TextHandle) -> tuple[int, int]:
    """
    Read the first line of a grid specification, which provides the
    dimensions of the grid. The format is:
    <row count> <blankspace> <column count>

    For example, the following indicates two rows and three columns.
    2 3

    :param input_fh: I/O handle from which to read grid spec.
    :return tuple consisting of a pair of integers: (rows, columns)
    """
    line = input_fh.readline().strip()
    (rows, cols) = line.split()
    rows = int(rows)
    cols = int(cols)
    return rows, cols


def read_grid_spec(input_fh: TextHandle) -> Optional[list[list]]:
    """
    Read one grid specification from input filehandle, then convert
    to structured representation.

    The first line of grid spec is the dimensions; see read_dimens().
    This is followed by a number of lines, as specified by the row count.
    Each line contains a number of characters, as specified by the column count.
    That character is always either '*' (asterisk) or '.' (dot).
    All lines are terminated by newline.

    The structured grid representation is a list of lists, wherein each inner
    list represents a row in the grid, and the elements of each inner list
    are single characters, same as read from the input grid spec.
    then write grid to output filehandle.

    :param input_fh: I/O handle from which to read grid spec.
    :return: None, if dimensions are 0x0;
    otherwise, structured representation of grid specification.
    """
    (rows, cols) = read_dimens(input_fh)
    if rows == 0 and cols == 0:
        return None

    grid = []
    while rows > 0:
        line = input_fh.readline().strip()
        cells = list(line)
        grid.append(cells)
        rows -= 1
    return grid


def add_grid_hints_one(grid: list[list]) -> None:
    """
    For every cell in structured grid representation, replace its
    content `.` (no mine) with count of neighboring cells with content
    `*` (has mine). Note suchs counts are of type int, not str.
    The grid is modified in-place.

    :param grid: The grid on which to operate. A lists of lists.
    :return None.
    """
    rows: int = len(grid)
    cols: int = len(grid[0])
    for y in range(rows):
        for x in range(cols):
            # Cell contains mine, leave as-is
            if grid[y][x] == '*':
                continue
            # Count number of mines in neighboring cells
            nbr_mines: int = 0
            for nbr_y in range(y-1, y+2):
                # Invalid coord, would be above/below grid
                if not 0 <= nbr_y < rows:
                    continue
                for nbr_x in range(x-1, x+2):
                    # Invalid coord, would be left/right of grid
                    if not 0 <= nbr_x < cols:
                        continue
                    # Already checked self above (redundant, albeit harmless)
                    if nbr_y == y and nbr_x == x:
                        continue
                    if grid[nbr_y][nbr_x] == '*':
                        nbr_mines += 1
            grid[y][x] = nbr_mines


def write_grid(grid: list[list], output_fh: TextHandle) -> None:
    """
    Convert structured grid representation back to string,
    and write to output filehandle.

    :param grid: Structured grid representation to convert.
    :param output_fh: I/O handle to which string is written.
    :return: None.
    """
    for row in grid:
        output_fh.write(''.join([str(cell) for cell in row]))
        output_fh.write('\n')


def xlate_grids(input_fh: TextHandle, output_fh: TextHandle):
    """
    Read a series of grid specifications from input filehandle,
    replace `.` marker of non-mine cells with a hint consisting of
    a count of immediately neighboring cells that contain a mine.
    Write the modified grid specs to output filehandle.
    Each output grid spec is prefixed by "Field #<index>:" where
    <count> is the 1-indexed position of the grid within the series.
    Each output grid spec is followed by empty line.
    All lines are terminated with newline.

    :param input_fh: Input I/O handle.
    :param output_fh: Output I/O handle.
    :return: None.
    """
    grid = read_grid_spec(input_fh)
    field_num = 1
    while grid is not None:
        output_fh.write(f'Field #{field_num}:\n')
        add_grid_hints_one(grid)
        write_grid(grid=grid, output_fh=output_fh)
        output_fh.write('\n')
        grid = read_grid_spec(input_fh)
        if grid is not None:
            field_num += 1


if __name__ == '__main__':
    import argparse as m_ap
    g_ap = m_ap.ArgumentParser(formatter_class=m_ap.ArgumentDefaultsHelpFormatter)
    g_ap.add_argument('--infile', type=str,
                      default=g_dflt_infile, help=f'Path to input file.')
    g_ap.add_argument('--outfile', type=str,
                      default=g_dflt_outfile, help=f'Path to output file.')
    g_a = g_ap.parse_args()

    with open(g_a.infile, 'r') as g_i_fh, open(g_a.outfile, 'w') as g_o_fh:
        xlate_grids(input_fh=g_i_fh, output_fh=g_o_fh)

# END
