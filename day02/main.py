from collections import Counter
from functools import reduce
from operator import mul, or_
from typing import NamedTuple, Self

class Game(NamedTuple):
    id: int
    hands: tuple[Counter[str], ...]
    @classmethod
    def from_line(cls, line: str) -> Self:
        head, tail = line.split(": ")
        id = int(head[5:])
        hands = tuple(
            Counter({color: int(n) for n, color in (pair.split() for pair in hand.split(", "))})
            for hand in tail.split("; ")
        )
        return cls(id, hands)

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
games = tuple(map(Game.from_line, raw.strip().splitlines()))

print(sum(g.id for g in games if all(h <= Counter(red=12, green=13, blue=14) for h in g.hands)))
print(sum(reduce(mul, reduce(or_, g.hands).values()) for g in games))
