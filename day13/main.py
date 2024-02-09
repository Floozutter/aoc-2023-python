from typing import NamedTuple, Self

class Pattern(NamedTuple):
    rows: tuple[tuple[bool, ...], ...]
    @classmethod
    def from_section(cls, section: str) -> Self:
        return cls(tuple(tuple(c == "#" for c in line) for line in section.splitlines()))
    def summary(self) -> int:
        return 0

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
patterns = tuple(map(Pattern.from_section, raw.strip().split("\n\n")))

print(sum(map(Pattern.summary, patterns)))
