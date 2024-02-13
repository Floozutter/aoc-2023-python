from itertools import groupby
from typing import Iterable, NamedTuple, Self

class Record(NamedTuple):
    blocks: tuple[int, ...]
    sizes: tuple[int, ...]
    @classmethod
    def from_parts(cls, pattern: str, sizes: Iterable[int]) -> Self:
        pairs = ((c, sum(1 for _ in group)) for c, group in groupby(pattern))
        return cls(tuple(n if c == "#" else -n if c == "?" else 0 for c, n in pairs), tuple(sizes))
    def unfold(self) -> Self:
        pattern = "".join("#"*b if b > 0 else "?"*-b if b < 0 else "." for b in self.blocks)
        return type(self).from_parts("?".join((pattern,)*5), self.sizes*5)

def arrangements(rec: Record) -> int:
    return 0

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
records = tuple(
    Record.from_parts(pattern, map(int, tail.split(",")))
    for pattern, tail in map(str.split, raw.strip().splitlines())
)

print(sum(arrangements(r) for r in records))
print(sum(arrangements(r.unfold()) for r in records))
