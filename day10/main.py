INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
tiles = {(i, j): t for i, line in enumerate(raw.strip().splitlines()) for j, t in enumerate(line)}

si, sj = next(p for p, t in tiles.items() if t == "S")
connections = {
    (i, j): (
        ((i-1, j), (i+1, j)) if t == "|" else
        ((i, j-1), (i, j+1)) if t == "-" else
        ((i-1, j), (i, j+1)) if t == "L" else
        ((i-1, j), (i, j-1)) if t == "J" else
        ((i+1, j), (i, j-1)) if t == "7" else
        ((i+1, j), (i, j+1)) if t == "F" else
        ()
    ) for (i, j), t in tiles.items()
}
connections[si, sj] = tuple(
    p for p in ((si-1, sj), (si, sj-1), (si, sj+1), (si+1, sj))
    if p in connections and (si, sj) in connections[p]
)

i = 0
visited = {(si, sj)}
frontier = frozenset(((si, sj),))
while (frontier := frozenset(q for p in frontier for q in connections[p] if q not in visited)):
    visited.update(frontier)
    i += 1
print(i)

sa, sb = 3*si + 1, 3*sj + 1
subtiles = {
    (3*i + da, 3*j + db): st
    for (i, j), t in tiles.items()
    for da, subtilerow in enumerate(
        ((0, 1, 0), (0, 1, 0), (0, 1, 0)) if t == "|" else
        ((0, 0, 0), (1, 1, 1), (0, 0, 0)) if t == "-" else
        ((0, 1, 0), (0, 1, 1), (0, 0, 0)) if t == "L" else
        ((0, 1, 0), (1, 1, 0), (0, 0, 0)) if t == "J" else
        ((0, 0, 0), (1, 1, 0), (0, 1, 0)) if t == "7" else
        ((0, 0, 0), (0, 1, 1), (0, 1, 0)) if t == "F" else
        ((0, 0, 0), (0, 2, 0), (0, 0, 0)) if t == "S" else
        ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    )
    for db, st in enumerate(subtilerow)
}
for da, db in ((-1, 0), (0, -1), (0, 1), (1, 0)):
    if subtiles.get((sa + 2*da, sb + 2*db), 0):
        subtiles[sa + da, sb + db] = 2
