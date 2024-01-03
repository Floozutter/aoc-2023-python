import re

INPUTPATH = "input.txt"
#INPUTPATH = "input-test1.txt"
#INPUTPATH = "input-test2.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
lines = raw.strip().split()

def part1(s: str) -> int:
    digits = "".join(c for c in s if c.isdigit())
    return 10*int(digits[0]) + int(digits[-1])

digit_values = (
    {str(i):i for i in range(1, 10)} |
    {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
)
digit_pattern = "|".join(digit_values.keys())
def part2(s: str) -> int:
    # re.findall can fail to find last because it searches for non-overlapping matches only
    first = re.search(digit_pattern, s)
    last = re.search(f"(?s:.*)({digit_pattern})", s)  # https://stackoverflow.com/a/33233868
    assert first is not None and last is not None
    return 10*digit_values[first[0]] + digit_values[last[1]]

print(sum(map(part1, lines)))
print(sum(map(part2, lines)))
