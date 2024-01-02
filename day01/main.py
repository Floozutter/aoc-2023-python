INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
lines = raw.strip().split()

def calibration(s: str) -> int:
    digits = "".join(c for c in s if c.isdigit())
    return 10*int(digits[0]) + int(digits[-1])
print(sum(map(calibration, lines)))
