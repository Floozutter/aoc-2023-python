INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
head, tail = raw.strip().split("\n\n")
workflows = {
    l: tuple(r[:-1].split(","))
    for l, r in (line.split("{") for line in head.split())
}
parts = tuple(
    {l: int(r) for l, r in (s.split("=") for s in line[1:-1].split(","))}
    for line in tail.split()
)
