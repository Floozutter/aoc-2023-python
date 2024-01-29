INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
subtiles = {
    (3*a + di, 3*b + dj): st
    for a, line in enumerate(raw.strip().splitlines()) for b, t in enumerate(line)
    for di, subtilerow in enumerate(
        ((0, 1, 0), (0, 1, 0), (0, 1, 0)) if t == "|" else
        ((0, 0, 0), (1, 1, 1), (0, 0, 0)) if t == "-" else
        ((0, 1, 0), (0, 1, 1), (0, 0, 0)) if t == "L" else
        ((0, 1, 0), (1, 1, 0), (0, 0, 0)) if t == "J" else
        ((0, 0, 0), (1, 1, 0), (0, 1, 0)) if t == "7" else
        ((0, 0, 0), (0, 1, 1), (0, 1, 0)) if t == "F" else
        ((0, 0, 0), (0, 2, 0), (0, 0, 0)) if t == "S" else
        ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    )
    for dj, st in enumerate(subtilerow)
}

si, sj = next(p for p, st in subtiles.items() if st == 2)
for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
    subtiles[si + di, sj + dj] = subtiles.get((si + 2*di, sj + 2*dj), 0)

visited = {(si, sj)}
frontier = frozenset(((si, sj),))
while (frontier := frozenset(
    (i + di, j + dj)
    for i, j in frontier for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0))
    if subtiles.get((i + di, j + dj), 0) == 1
)):
    subtiles.update({p: 2 for p in frontier})
    visited.update(frontier)
print(len(visited)//6)

cache: dict[tuple[int, int], bool] = {}
def enclosed(i: int, j: int, visited: frozenset[tuple[int, int]] = frozenset()) -> bool:
    if (i, j) not in cache:
        cache[i, j] = (i, j) in subtiles and subtiles[i, j] == 0 and all(
            subtiles.get((i + di, j + dj), 0) == 2 or enclosed(i + di, j + dj, frozenset((*visited, (i, j))))
            for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0))
            if (i + di, j + dj) not in visited
        )
    return cache[i, j]

print(sum(
    1 for a in range(max(subtiles)[0]//3) for b in range(max(subtiles)[1]//3)
    if all(enclosed(3*a + di, 3*b + dj) for di in range(3) for dj in range(3))
))
