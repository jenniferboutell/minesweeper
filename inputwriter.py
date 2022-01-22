import random


columns = input("Please enter the Number of Columns you would like to test: ")
rows = input("Please enter the number of rows you would like to test: ")
minepercentage = input("Please enter the percentage of mines you would like to test: ")


mine_input = open('input.txt', 'w')

def writeinput():
    for y in range(0, int(rows)):
        for x in range(0, int(columns)):
            if random.randrange(0, 100) < int(minepercentage):
                mine_input.write("*")
            else:
                mine_input.write(".")
        mine_input.write("\n")
if minepercentage.isnumeric() == False or rows.isnumeric() == False or columns.isnumeric() == False:
    print("Minefield not generated. Please enter valid integers between 0 and 100")
else:
    if int(minepercentage) not in range(0, 100) or int(rows) not in range(0,100) or int(columns) not in range(0,100):
        print("Minefield not generated. Please enter valid integers between 0 and 100")
    else:
        writeinput()
