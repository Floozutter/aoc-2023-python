from typing import NamedTuple, Self

class Modu(NamedTuple):
    typu: str
    name: str
    dest: tuple[str, ...]
    @classmethod
    def from_line(cls, line: str) -> Self:
        return cls("", "", ())

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
