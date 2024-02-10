from itertools import combinations
from typing import NamedTuple, Self

class Record(NamedTuple):
    pattern: str
    groups: tuple[int, ...]
    @classmethod
    def from_line(cls, line: str) -> Self:
        pattern, tail = line.split()
        return cls(pattern, tuple(map(int, tail.split(","))))
    def arrangements(self) -> int:
        return 0
    def unfold(self) -> Self:
        return type(self)("?".join(5*(self.pattern,)), 5*self.groups)

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
records = tuple(map(Record.from_line, raw.strip().splitlines()))

print(sum(r.arrangements() for r in records))
print(sum(r.unfold().arrangements() for r in records))
