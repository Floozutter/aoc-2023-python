from itertools import combinations

def expand(galaxies: frozenset[tuple[int, int]]) -> frozenset[tuple[int, int]]:
    xs, ys = (list(column) for column in zip(*sorted(galaxies)))
    for i in range(len(xs) - 1):
        distance = xs[i+1] - xs[i]
        for j in range(i + 1, len(xs)):
            xs[j] += max(0, distance - 1)
    ys, xs = (list(column) for column in zip(*sorted(zip(ys, xs))))
    for i in range(len(ys) - 1):
        distance = ys[i+1] - ys[i]
        for j in range(i + 1, len(ys)):
            ys[j] += max(0, distance - 1)
    return frozenset(zip(xs, ys))

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
galaxies = frozenset(
    (x, y)
    for y, line in enumerate(raw.strip().splitlines()) for x, c in enumerate(line)
    if c == "#"
)

print(sum(abs(bx - ax) + abs(by - ay) for (ax, ay), (bx, by) in combinations(expand(galaxies), 2)))
