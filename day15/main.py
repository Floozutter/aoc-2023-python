def hashbrown(s: str) -> int:
    value = 0
    for c in s:
        value = (value + ord(c)) * 17 % 256
    return value

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
steps = tuple(raw.strip().split(","))

print(sum(map(hashbrown, steps)))
