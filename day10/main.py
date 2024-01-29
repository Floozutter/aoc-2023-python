INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
subtiles = {
    (3*a + di, 3*b + dj): st
    for a, line in enumerate(raw.strip().splitlines()) for b, c in enumerate(line)
    for di, subtilerow in enumerate(
        ((0, 1, 0), (0, 1, 0), (0, 1, 0)) if c == "|" else
        ((0, 0, 0), (1, 1, 1), (0, 0, 0)) if c == "-" else
        ((0, 1, 0), (0, 1, 1), (0, 0, 0)) if c == "L" else
        ((0, 1, 0), (1, 1, 0), (0, 0, 0)) if c == "J" else
        ((0, 0, 0), (1, 1, 0), (0, 1, 0)) if c == "7" else
        ((0, 0, 0), (0, 1, 1), (0, 1, 0)) if c == "F" else
        ((0, 0, 0), (0, 2, 0), (0, 0, 0)) if c == "S" else
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
