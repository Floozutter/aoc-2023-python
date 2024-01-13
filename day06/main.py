from math import ceil, floor, prod, sqrt

def winners(time: int, record: int) -> int:
    lower = (time-sqrt(time**2-4*record))/2
    upper = (time+sqrt(time**2-4*record))/2
    return ceil(upper) - floor(lower) - 1

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
times, records = (tuple(map(int, line.split()[1:])) for line in raw.strip().splitlines())
print(prod(winners(t, r) for t, r in zip(times, records)))

time, record = int("".join(map(str, times))), int("".join(map(str, records)))
print(winners(time, record))
