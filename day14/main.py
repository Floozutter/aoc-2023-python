def tilt_left(s: str) -> str:
    cubes = (-1, *(i for i, c in enumerate(s) if c == "#"), len(s))
    return "".join(
        "#" + "O"*s[l+1:r].count("O") + "."*s[l+1:r].count(".")
        for l, r in zip(cubes, cubes[1:])
    )[1:]

def load_left(s: str) -> int:
    return sum(len(s) - i for i, c in enumerate(s) if c == "O")

def rotate(rows: tuple[str, ...], times: int) -> tuple[str, ...]:
    for _ in range(times):
        rows = tuple(map("".join, zip(*reversed(rows))))
    return rows

def tilt(platform: tuple[str, ...], direction: int) -> tuple[str, ...]:
    return rotate(tuple(map(tilt_left, rotate(platform, direction))), 4 - direction)

def load(platform: tuple[str, ...], direction: int) -> int:
    return sum(map(load_left, rotate(platform, direction)))

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
platform = tuple(raw.strip().splitlines())

print(load(tilt(platform, 3), 3))
