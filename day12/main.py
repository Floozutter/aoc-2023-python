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
        return cls(tuple(sum(group) for _, group in groupby(ungrouped, sign)), tuple(sizes))
    def unfold(self) -> Self:
        u = (*self.groups, -1, *self.groups, -1, *self.groups, -1, *self.groups, -1, *self.groups)
        return type(self).from_ungrouped(u, self.sizes*5)

def arrangements(rec: Record) -> int:
    """
    unknown = next((b for b in rec.blocks if b < 0), None)
    known_sizes = tuple(b for b in rec.blocks if b > 0)
    if unknown is None or sum(known_sizes) >= rec.sizes:
        return known_sizes == rec.sizes
    """
    return 0

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
records = tuple(map(Record.from_line, raw.strip().splitlines()))

print(sum(arrangements(r) for r in records))
print(sum(arrangements(r.unfold()) for r in records))
