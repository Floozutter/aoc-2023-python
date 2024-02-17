INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
platform = {(i, j): c for i, line in enumerate(raw.splitlines()) for j, c in enumerate(line)}
