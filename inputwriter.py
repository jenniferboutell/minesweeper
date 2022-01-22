from typing import TextIO
import random


def writeinput(rows: int, columns: int, minepercentage: int, file: TextIO):
    for y in range(0, rows):
        for x in range(0, columns):
            if random.randrange(0, 100) < minepercentage:
                file.write("*")
            else:
                file.write(".")
        file.write("\n")


if __name__ == '__main__':
    g_cols = input("Please enter the Number of Columns you would like to test: ")
    g_rows = input("Please enter the number of rows you would like to test: ")
    g_perc = input("Please enter the percentage of mines you would like to test: ")
    g_file = open('input.txt', 'w')

    if not g_perc.isnumeric() or not g_rows.isnumeric() or not g_cols.isnumeric():
        print("Minefield not generated. Please enter valid integers.")
    else:
        g_cols = int(g_cols)
        g_rows = int(g_rows)
        g_perc = int(g_perc)
        if not 0 <= g_perc <= 100:
            print("Minefield not generated. Please enter percentage between 0 and 100.")
        if g_rows <= 0 or g_cols <= 0:
            print("Minefield not generated. Please enter positive integers for row and column counts.")
        else:
            writeinput(rows=g_rows, columns=g_cols, minepercentage=g_perc, file=g_file)

# END
