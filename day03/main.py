import itertools

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
grid = tuple(raw.strip().split())

def adjacents(i: int, j: int) -> tuple[tuple[int, int], ...]:
    return (i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j+0), (i+1,j+1)

visited: set[tuple[int, int]] = set()
def find_number(i: int, j: int) -> int | None:
    def f(j: int, recur_left: bool, recur_right: bool) -> str:
        if (i, j) in visited:
            return ""
        visited.add((i, j))
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j].isdigit():
            l = f(j-1, True, False) if recur_left else ""
            r = f(j+1, False, True) if recur_right else ""
            return l + grid[i][j] + r
        return ""
    number = f(j, True, True)
    return None if not number else int(number)

parts = tuple(itertools.chain.from_iterable(
    (n for n in (find_number(x, y) for x, y in adjacents(i, j)) if n is not None)
    for i, row in enumerate(grid)
    for j, c in enumerate(row)
    if c != "." and not c.isdigit()
))
print(sum(parts))
