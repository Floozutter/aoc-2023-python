INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
layout = {(i, j): c for i, line in enumerate(raw.strip().splitlines()) for j, c in enumerate(line)}