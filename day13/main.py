from typing import NamedTuple, Sequence

class Reflection(NamedTuple):
    score: int
    idx: int
    vertical: bool

def reflections(rows: Sequence[Sequence[bool]]) -> Sequence[Reflection]:
    def row_reflections(rows: Sequence[Sequence[bool]], vertical: bool) -> Sequence[Reflection]:
        return ()
    return ()

def horizontal_reflection(rows: tuple[tuple[bool, ...], ...]) -> None | int:
    for i in range(len(rows) - 1):
        if all(rows[i-n] == rows[i+1+n] for n in range(min(i+1, len(rows)-i-1))):
            return i
    return None

def summarize(rows: tuple[tuple[bool, ...], ...]) -> int:
    if (horizontal := horizontal_reflection(rows)) is not None:
        return 100 * (horizontal + 1)
    transposed = tuple(tuple(column) for column in zip(*rows))
    if (vertical := horizontal_reflection(transposed)) is not None:
        return vertical + 1
    raise ValueError

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
patterns = tuple(
    tuple(tuple(c == "#" for c in line) for line in section.splitlines())
    for section in raw.strip().split("\n\n")
)

print(sum(map(summarize, patterns)))
