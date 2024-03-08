from typing import NamedTuple, Self

class Beam(NamedTuple):
    i: int; j: int
    di: int; dj: int
    def step(self, tile: str) -> tuple[Self, ...]:
        i, j, di, dj = self
        if tile != ".":
            return ()
        else:
            return (type(self)(i+di, j+dj, di, dj),)

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
layout = {(i, j): c for i, line in enumerate(raw.strip().splitlines()) for j, c in enumerate(line)}

beams = frozenset((Beam(0, 0, 0, 1),))
seen = set(beams)
energized = set((b.i, b.j) for b in beams)
while beams := frozenset(
    y for x in beams for y in x.step(layout[x.i, x.j]) if (y.i, y.j) in layout and y not in seen
):
    seen.update(beams)
    energized.update((b.i, b.j) for b in beams)
print(len(energized))
