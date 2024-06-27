import sys
import backtrack
import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Expects 3 arguments, received {len(sys.argv)}")
        exit(1)

    type = str(sys.argv[1])
    file_name = str(sys.argv[2])
    puzzle = backtrack.parse_puzzle(file_name)

    solution = pd.DataFrame()
    if type == "-n":
        solution = backtrack.naive_backtrack(puzzle)
    elif type == "-m":
        solution = backtrack.mrv_backtrack(puzzle)
    else:
        print("Invalid flag: use -n for naive solve and -m for MRV solve")
        exit(1)

    if solution is not None:
        print("Solution found")
        if backtrack.validate(solution):
            print(solution)
    else:
        print("Solution does not exist")
