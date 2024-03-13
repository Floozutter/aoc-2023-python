from typing import NamedTuple, Self

class Dig(NamedTuple):
    di: int; dj: int
    r: int; g: int; b: int
    @classmethod
    def from_line(cls, line: str) -> Self:
        l, m, r = line.split()
        d = int(m)
        return cls(
            *((d, 0) if l == "D" else (0, d) if l == "R" else (-d, 0) if l == "U" else (0, -d)),
            *(int(r[i+2:i+4], 16) for i in (0, 2, 4))
        )

def range_to(z: int) -> range:
    return range(0, z+1 if z >= 0 else z-1, 1 if z >= 0 else -1)

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
plan = tuple(map(Dig.from_line, raw.strip().splitlines()))

trench = set(((0, 0),))
i, j = 0, 0
for dig in plan:
    trench.update((i+di, j+dj) for di in range_to(dig.di) for dj in range_to(dig.dj))
    i, j = i+dig.di, j+dig.dj
