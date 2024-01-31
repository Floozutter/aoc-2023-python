INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
galaxies = {(i, j) for i, line in raw.strip().splitlines() for j, c in line if c == "#"}
