from itertools import combinations

def distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def expand(galaxies: frozenset[tuple[int, int]], scale: int) -> frozenset[tuple[int, int]]:
    xs, ys = (list(column) for column in zip(*sorted(galaxies)))
    for i in range(len(xs) - 1):
        skipped = max(0, xs[i+1] - xs[i] - 1)
        for j in range(i + 1, len(xs)):
            xs[j] += skipped * (scale - 1)
    ys, xs = (list(column) for column in zip(*sorted(zip(ys, xs))))
    for i in range(len(ys) - 1):
        skipped = max(0, ys[i+1] - ys[i] - 1)
        for j in range(i + 1, len(ys)):
            ys[j] += skipped * (scale - 1)
    return frozenset(zip(xs, ys))

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
galaxies = frozenset(
    (x, y) for y, s in enumerate(raw.strip().splitlines()) for x, c in enumerate(s) if c == "#"
)

print(sum(distance(a, b) for a, b in combinations(expand(galaxies, 2), 2)))
print(sum(distance(a, b) for a, b in combinations(expand(galaxies, 1_000_000), 2)))
