from typing import Iterator, NamedTuple, Sequence

class Reflection(NamedTuple):
    diff: int
    i: int
    vert: bool

def ordered_reflections(rows: Sequence[Sequence[bool]]) -> Sequence[Reflection]:
    def row_reflections(rows: Sequence[Sequence[bool]], vert: bool) -> Iterator[Reflection]:
        for i in range(len(rows)-1):
            diff = sum(
                sum(a != b for a, b in zip(rows[i-n], rows[i+1+n]))
                for n in range(min(i+1, len(rows)-i-1))
            )
            yield Reflection(diff, i, vert)
    transposed = tuple(tuple(column) for column in zip(*rows))
    reflections = (*row_reflections(rows, False), *row_reflections(transposed, True))
    return tuple(sorted(reflections))

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
orderings = tuple(
    ordered_reflections(tuple(tuple(c == "#" for c in line) for line in section.splitlines()))
    for section in raw.strip().split("\n\n")
)

firsts, seconds = zip(*((first, second) for first, second, *_ in orderings))
print(sum(r.i+1 if r.vert else 100*(r.i+1) for r in firsts))
print(sum(r.i+1 if r.vert else 100*(r.i+1) for r in seconds))
