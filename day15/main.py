def hashbrown(s: str, value: int = 0) -> int:
    return value if not s else hashbrown(s[1:], (value + ord(s[0])) * 17 % 256)

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
steps = tuple(raw.strip().split(","))

print(sum(map(hashbrown, steps)))

boxes: tuple[list[tuple[str, int]], ...] = tuple([] for _ in range(256))
for s in steps:
    opi = next(i for i, c in enumerate(s) if not c.isalpha())
    label = s[:opi]
    box = boxes[hashbrown(label)]
    sloti = next((i for i, (l, _) in enumerate(box) if l == label), None)
    if s[opi] == "-":
        if sloti is not None:
            box.pop(sloti)
    else:
        focal = int(s[opi+1:])
        if sloti is not None:
            box[sloti] = (label, focal)
        else:
            box.append((label, focal))
print(sum((i+1)*(j+1)*f for i, box in enumerate(boxes) for j, (_, f) in enumerate(box)))
