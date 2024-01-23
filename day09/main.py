INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
histories = tuple(tuple(map(int, line.split())) for line in raw.strip().splitlines())
