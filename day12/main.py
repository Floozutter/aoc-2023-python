from typing import NamedTuple, Self

class Record(NamedTuple):
    pattern: str
    groups: tuple[int, ...]
    @classmethod
    def from_line(cls, line: str) -> Self:
        pattern, tail = line.split()
        return cls(pattern, tuple(map(int, tail.split(","))))

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
records = tuple(map(Record.from_line, raw.strip().splitlines()))
