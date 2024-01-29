ADJACENTS = ((-1, 0), (0, -1), (0, 1), (1, 0))

INPUTPATH = "input.txt"
#INPUTPATH = "input-test1.txt"
#INPUTPATH = "input-test2.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
tiles = {(a, b): t for a, line in enumerate(raw.strip().splitlines()) for b, t in enumerate(line)}

si, sj = next((3*a + 1, 3*b + 1) for (a, b), t in tiles.items() if t == "S")
subtiles = {
    (3*a + di, 3*b + dj): st
    for (a, b), t in tiles.items()
    for di, subtilerow in enumerate(
        ((0, 1, 0), (0, 1, 0), (0, 1, 0)) if t == "|" else
        ((0, 0, 0), (1, 1, 1), (0, 0, 0)) if t == "-" else
        ((0, 1, 0), (0, 1, 1), (0, 0, 0)) if t == "L" else
        ((0, 1, 0), (1, 1, 0), (0, 0, 0)) if t == "J" else
        ((0, 0, 0), (1, 1, 0), (0, 1, 0)) if t == "7" else
        ((0, 0, 0), (0, 1, 1), (0, 1, 0)) if t == "F" else
        ((0, 0, 0), (0, 1, 0), (0, 0, 0)) if t == "S" else
        ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    )
    for dj, st in enumerate(subtilerow)
}
for di, dj in ADJACENTS:
    subtiles[si + di, sj + dj] = subtiles.get((si + 2*di, sj + 2*dj), 0)

def contigous_subtiles(pos: tuple[int, int]) -> set[tuple[int, int]]:
    contiguous = {pos}
    frontier = frozenset(contiguous)
    while (frontier := frozenset(
        (i + di, j + dj)
        for i, j in frontier for di, dj in ADJACENTS
        if subtiles.get((i + di, j + dj)) == subtiles[pos] and (i + di, j + dj) not in contiguous
    )):
        contiguous |= frontier
    return contiguous

pipeloop = contigous_subtiles((si, sj))
print(len(pipeloop) // 6)

subtiles.update({pos: 0 for pos in subtiles if pos not in pipeloop})

enclosed: set[tuple[int, int]] = set()
unchecked = {pos for pos, st in subtiles.items() if st == 0}
while unchecked:
    region = contigous_subtiles(unchecked.pop())
    if all((i + di, j + dj) in subtiles for i, j in region for di, dj in ADJACENTS):
        enclosed |= region
    unchecked -= region

print(sum(
    1 for a, b in tiles
    if all((3*a + di, 3*b + dj) in enclosed for di in range(3) for dj in range(3))
))
