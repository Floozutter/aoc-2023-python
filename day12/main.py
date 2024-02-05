from itertools import combinations
from typing import NamedTuple, Self, Iterator

class Record(NamedTuple):
    pattern: str
    groups: tuple[int, ...]
    @classmethod
    def from_line(cls, line: str) -> Self:
        pattern, tail = line.split()
        return cls(pattern, tuple(map(int, tail.split(","))))
    def arrangements(self) -> Iterator[str]:
        unknowns = tuple(i for i, c in enumerate(self.pattern) if c == "?")
        missing = sum(self.groups) - self.pattern.count("#")
        for damageds in (frozenset(comb) for comb in combinations(unknowns, missing)):
            a = "".join(
                c if c != "?" else "#" if i in damageds else "."
                for i, c in enumerate(self.pattern)
            )
            if tuple(len(g) for g in a.replace(".", " ").strip().split()) == self.groups:
                yield a
    def unfold(self) -> Self:
        return type(self)("?".join(5*(self.pattern,)), 5*self.groups)

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
records = tuple(map(Record.from_line, raw.strip().splitlines()))

print(sum(1 for r in records for a in r.arrangements()))
print(sum(1 for r in records for a in r.unfold().arrangements()))
