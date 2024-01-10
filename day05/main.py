from functools import reduce
from typing import NamedTuple, Self

class Map(NamedTuple):
    ranges: tuple[tuple[int, int, int], ...]
    @classmethod
    def from_section(cls, section: str) -> Self:
        return cls(tuple(
            (a, b, c) for a, b, c in (map(int, line.split()) for line in section.splitlines()[1:])
        ))
    def convert(self, n: int) -> int:
        for dest_start, source_start, size in self.ranges:
            diff = n - source_start
            if 0 <= diff < size:
                return diff + dest_start
        return n

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
head, *rest = raw.strip().split("\n\n")
seeds = tuple(map(int, head[7:].split()))
maps = tuple(map(Map.from_section, rest))

print(min(reduce(lambda n, m: m.convert(n), maps, n) for n in seeds))
