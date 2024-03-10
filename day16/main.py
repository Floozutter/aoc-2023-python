from typing import NamedTuple, Self

class Beam(NamedTuple):
    i: int; j: int
    di: int; dj: int
    def step(self, tile: str) -> tuple[Self, ...]:
        i, j, di, dj = self.i, self.j, self.di, self.dj
        if tile == "-" and di:
            return (type(self)(i, j-1, 0, -1), type(self)(i, j+1, 0, 1))
        elif tile == "|" and dj:
            return (type(self)(i-1, j, -1, 0), type(self)(i+1, j, 1, 0))
        elif tile == "/":
            return (type(self)(i-dj, j-di, -dj, -di),)
        elif tile == "\\":
            return (type(self)(i+dj, j+di, dj, di),)
        else:
            return (type(self)(i+di, j+dj, di, dj),)

def energized(grid: dict[tuple[int, int], str], starter: Beam) -> int:
    beams = frozenset((starter,))
    made = set(beams)
    visited = set((b.i, b.j) for b in beams)
    while beams := frozenset(
        y for x in beams for y in x.step(grid[x.i, x.j]) if (y.i, y.j) in grid and y not in made
    ):
        made.update(beams)
        visited.update((b.i, b.j) for b in beams)
    return len(visited)

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
grid = {(i, j): c for i, line in enumerate(raw.strip().splitlines()) for j, c in enumerate(line)}

print(energized(grid, Beam(0, 0, 0, 1)))
print(max(
    energized(grid, Beam(i, j, di, dj))
    for i, j in grid for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1))
    if (i-di, j-dj) not in grid
))
