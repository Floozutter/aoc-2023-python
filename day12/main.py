from functools import cache
from itertools import groupby
from typing import Iterable, NamedTuple, Self

class Record(NamedTuple):
    groups: tuple[int, ...]
    sizes: tuple[int, ...]
    @classmethod
    def from_line(cls, line: str) -> Self:
        head, tail = line.split()
        groups = tuple(1 if c == "#" else -1 if c == "?" else 0 for c in head)
        return cls(groups, tuple(map(int, tail.split(","))))
    def reduce(self) -> Self:
        sign = lambda n: 1 if n > 0 else -1 if n < 0 else 0
        groups = tuple(sum(values) for _, values in groupby(self.groups, sign))
        sizes = self.sizes
        while groups:
            if groups[0] == 0:
                groups = groups[1:]
            elif groups[-1] == 0:
                groups = groups[:-1]
            elif sizes and groups[0] == sizes[0] and (len(groups) == 1 or groups[1] == 0):
                groups = groups[1:]
                sizes = sizes[1:]
            elif sizes and groups[-1] == sizes[-1] and (len(groups) == 1 or groups[-2] == 0):
                groups = groups[:-1]
                sizes = sizes[:-1]
            else:
                break
        return type(self)(groups, sizes)
    def unfold(self) -> Self:
        g = self.groups
        return type(self)((*g, -1, *g, -1, *g, -1, *g, -1, *g), self.sizes*5)

@cache
def arrangements(rec: Record) -> int:
    i = next((i for i, g in enumerate(rec.groups) if g < 0), None)
    known_sizes = tuple(g for g in rec.groups if g > 0)
    if i is None or sum(known_sizes) >= sum(rec.sizes):
        return known_sizes == rec.sizes
    head = rec.groups[:i]
    tail = ((rec.groups[i]+1,) if rec.groups[i]+1 < 0 else ()) + rec.groups[i+1:]
    a = arrangements(Record((*head, 0, *tail), rec.sizes).reduce())
    b = arrangements(Record((*head, 1, *tail), rec.sizes).reduce())
    return a + b

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
records = tuple(map(Record.from_line, raw.strip().splitlines()))

print(sum(arrangements(r.reduce()) for r in records))
print(sum(arrangements(r.unfold().reduce()) for r in records))
