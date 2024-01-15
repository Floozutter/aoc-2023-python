INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
pairs = tuple((l, int(r)) for l, r in map(str.split, raw.strip().splitlines()))
