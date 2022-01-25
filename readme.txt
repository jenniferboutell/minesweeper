# TCSS 504 Winter 2022 - Group Assignment 1
# minesweeper

Students: Darence Thong, Jennifer Boutell, JP Montagnet

Time spent:
Darence - 3 hours
  Hint producing code function method
  Some unit tests
  Comparing input and output
  
Jennifer - 4.5 hours
  Input Generator Solution
  Packaging and readme
  repository maintenance
  
JP - 4.5 hours
  This project is based on JP's solution to the individual assignment.
  Most unit tests
  Debugging and troubleshooting
  
Note on input/output filenames:
When run with no arguments, minemapper.py defaults to input.txt and output.txt
as the names of its input/output files, respectively. These names were chosen
to not conflict with any of the filenames mandated as part of the assignment
submission and/or checked into the team's GitHub repo for the assignment.
To test the solution, specify the desired filenames as command-line options;
for example:

  minemapper.py --infile official_input.txt --outfile my_output.txt

Note on unit-tests:
Requires that pytest has been installed in your Python environment.

Files carried over from the individual assignment:
- minesweeper.py
    The "solution", i.e. the program that reads a series of minefield specs,
    adds the hints, and outputs with tper-field headers adjusted per instructions.
    Except for minor cosmetic changes, re-used JP's individual solution as-is.
- official_input.txt
    One series of minefield specs, exercsing various scenarios.
- official_output.txt
    The expected (and actual) result of running minesweeper.py
    against official_input.txt.
- field_combos.csv
    A summary of dimensions and percentages of each minefield in official_input.txt.
    Used later when running minefield generator. (see below)

Files new in the team assignment:
- inputwriter.py
    Our minefield spec generator.
- minesweeper_input.txt
    Another series of minefield specs, as produced by inputwriter.py.
    Used field_combos.csv for its parameters, and thus is similar to
    official_input.txt, except for positions of individual mines.
- minesweeper_output.txt
    The expected (and actual) result of running minesweeper.py
    against minesweeper_input.txt.
- inputwriter_capture.txt
    Console capture from running inputwriter.py, as described above.
- test_*.py
    Unit-tests for the functions in minesweeper.py.
- unittests_capture.py
    Console capture from running unit-tests, with 100% passing.

# END
