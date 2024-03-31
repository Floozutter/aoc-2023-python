from typing import NamedTuple, Self

class Modu(NamedTuple):
    typu: str
    name: str
    dest: tuple[str, ...]
    @classmethod
    def from_line(cls, line: str) -> Self:
        l, r = line.split(" -> ")
        return cls(l[0], l[1:], tuple(r.split(", ")))

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
