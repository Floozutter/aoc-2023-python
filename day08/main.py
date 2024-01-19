INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
instructions, tail = raw.strip().split("\n\n")
network = {l: (r[1:4], r[-4:-1]) for l, r in (line.split(" = ") for line in tail.splitlines())}
