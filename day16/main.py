from typing import NamedTuple, Self

class Beam(NamedTuple):
    i: int; j: int
    di: int; dj: int
    def step(self, tile: str) -> tuple[Self, ...]:
        return ()

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
layout = {(i, j): c for i, line in enumerate(raw.strip().splitlines()) for j, c in enumerate(line)}

beams = frozenset((Beam(0, 0, 0, 1),))
energized: set[tuple[int, int]] = set()
while beams:
    energized.update((b.i, b.j) for b in beams)
    beams = frozenset(y for x in beams for y in x.step(layout[x.i, x.j]) if (y.i, y.j) in layout)
print(len(energized))
