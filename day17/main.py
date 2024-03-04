INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
grid = {(i, j): int(c) for i, l in enumerate(raw.strip().splitlines()) for j, c in enumerate(l)}
