from functools import reduce
from typing import Iterable, NamedTuple, Self

class Interval(NamedTuple):
    start: int
    end: int
    def __len__(self) -> int:
        return self.end - self.start
    def __and__(self, other: Self) -> Self:
        start, end = max(self.start, other.start), min(self.end, other.end)
        return self.__class__(start, end) if start < end else self.__class__(0, 0)
    def __sub__(self, other: Self) -> tuple[()] | tuple[Self] | tuple[Self, Self]:
        if other.start <= self.start and self.end <= other.end:
            return ()
        elif other.start <= self.start < other.end:
            return self.__class__(other.end, self.end),
        elif other.start < self.end <= other.end:
            return self.__class__(self.start, other.start),
        elif self.start < other.start and other.end < self.end:
            return self.__class__(self.start, other.start), self.__class__(other.end, self.end)
        else:
            return self,

class Converter(NamedTuple):
    portals: tuple[tuple[Interval, Interval], ...]
    @classmethod
    def from_section(cls, section: str) -> Self:
        return cls(tuple(
            (Interval(b, b+size), Interval(a, a+size))
            for a, b, size in (map(int, line.split()) for line in section.splitlines()[1:])
        ))
    def convert(self, n: int) -> int:
        for source, dest in self.portals:
            if source.start <= n < source.end:
                return n - source.start + dest.start
        return n
    def convert_intervals(self, intervals: Iterable[Interval]) -> frozenset[Interval]:
        unconverted = set(intervals)
        converted: set[Interval] = set()
        while unconverted:
            val = unconverted.pop()
            for source, dest in self.portals:
                intersection = val & source
                if len(intersection) > 0:
                    offset = -source.start + dest.start
                    converted.add(Interval(intersection.start+offset, intersection.end+offset))
                    unconverted.update(val - source)
                    break
            else:
                converted.add(val)
        return frozenset(converted)

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
head, *rest = raw.strip().split("\n\n")
seeds = tuple(map(int, head[7:].split()))
converters = tuple(map(Converter.from_section, rest))

print(min(reduce(lambda n, c: c.convert(n), converters, n) for n in seeds))
print(min(reduce(
    lambda intervals, c: c.convert_intervals(intervals),
    converters,
    frozenset(Interval(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2))
)).start)
