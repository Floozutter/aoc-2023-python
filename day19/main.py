from typing import NamedTuple

class Part(NamedTuple):
    x: int; m: int; a: int; s: int
    def accepted_by(self, workflows: dict[str, tuple[str, ...]]) -> bool:
        return False

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
head, tail = raw.strip().split("\n\n")
workflows = {l: tuple(r[:-1].split(",")) for l, r in (line.split("{") for line in head.split())}
parts = tuple(
    Part(*(int(s[s.index("=")+1:]) for s in line[1:-1].split(",")))
    for line in tail.split()
)

print(sum(sum(p) for p in parts if p.accepted_by(workflows)))
