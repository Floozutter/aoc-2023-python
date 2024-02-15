from itertools import groupby
from typing import Iterable, NamedTuple, Self

class Record(NamedTuple):
    groups: tuple[int, ...]
    sizes: tuple[int, ...]
    @classmethod
    def from_line(cls, line: str) -> Self:
        head, tail = line.split()
        ungrouped = (1 if c == "#" else -1 if c == "?" else 0 for c in head)
        sizes = map(int, tail.split(","))
        return cls.from_ungrouped(ungrouped, sizes)
    @classmethod
    def from_ungrouped(cls, ungrouped: Iterable[int], sizes: Iterable[int]) -> Self:
        sign = lambda n: 1 if n > 0 else -1 if n < 0 else 0
        return cls(tuple(sum(values) for _, values in groupby(ungrouped, sign)), tuple(sizes))
    def unfold(self) -> Self:
        g = self.groups
        return type(self).from_ungrouped((*g, -1, *g, -1, *g, -1, *g, -1, *g), self.sizes*5)

def arrangements(rec: Record) -> int:
    i = next((i for i, g in enumerate(rec.groups) if g < 0), None)
    known_sizes = tuple(g for g in rec.groups if g > 0)
    if i is None or sum(known_sizes) >= sum(rec.sizes):
        return known_sizes == rec.sizes
    head = rec.groups[:i]
    tail = ((rec.groups[i]+1,) if rec.groups[i]+1 < 0 else ()) + rec.groups[i+1:]
    a = arrangements(Record.from_ungrouped((*head, 0, *tail), rec.sizes))
    b = arrangements(Record.from_ungrouped((*head, 1, *tail), rec.sizes))
    return a + b

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
records = tuple(map(Record.from_line, raw.strip().splitlines()))

print(sum(arrangements(r) for r in records))
print(sum(arrangements(r.unfold()) for r in records))
