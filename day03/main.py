from collections import defaultdict
from typing import NamedTuple

class Number(NamedTuple):
    value: int
    leftmost: tuple[int, int]
class Symbol(NamedTuple):
    value: str
    pos: tuple[int, int]

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
grid = tuple(raw.strip().split())
h, w = len(grid), len(grid[0])

number_adjacency: dict[Number, set[Symbol]] = {}
for i in range(h):
    j = 0
    while j < w:
        if grid[i][j].isdigit():
            k = j
            while k < w and grid[i][k].isdigit():
                k += 1
            number_adjacency[Number(int("".join(grid[i][p] for p in range(j, k))), (i, j))] = {
                Symbol(grid[a][b], (a, b))
                for a, b in (
                    *((i-1, p) for p in range(j-1,k+1)),
                    *((i+1, p) for p in range(j-1,k+1)),
                    (i, j-1), (i, k)
                )
                if 0 <= a < h and 0 <= b < w and grid[a][b] != "." and not grid[a][b].isdigit()
            }
            j = k
        j += 1
print(sum(number.value for number, symbols in number_adjacency.items() if symbols))

symbol_adjacency: dict[Symbol, set[Number]] = defaultdict(set)
for n, symbols in number_adjacency.items():
    for s in symbols:
        symbol_adjacency[s].add(n)
print(sum(x.value * y.value for x, y in filter(lambda s: len(s) == 2, symbol_adjacency.values())))
