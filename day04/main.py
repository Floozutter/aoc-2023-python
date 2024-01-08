from typing import NamedTuple, Self

class Card(NamedTuple):
    id: int
    winners: frozenset[int]
    numbers: frozenset[int]
    @classmethod
    def from_line(cls, line: str) -> Self:
        head, tail = line.split(": ")
        l, r = tail.split(" | ")
        return cls(int(head[5:]), frozenset(map(int, l.split())), frozenset(map(int, r.split())))

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
cards = tuple(map(Card.from_line, raw.strip().splitlines()))

print(sum(int(2 ** (len(c.winners & c.numbers) - 1)) for c in cards))
