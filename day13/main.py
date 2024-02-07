INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
patterns = tuple(
    {(i, j): c for i, line in enumerate(section.splitlines()) for j, c in enumerate(line)}
    for section in raw.strip().split("\n\n")
)
