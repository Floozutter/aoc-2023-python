INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
head, tail = raw.strip().split("\n\n")
workflows = {}
parts = tuple(
    {l: int(r) for l, r in (s.split("=") for s in line[1:-1].split(","))}
    for line in tail.split()
)
