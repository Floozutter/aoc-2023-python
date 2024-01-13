from math import prod

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
times, records = (tuple(map(int, line.split()[1:])) for line in raw.strip().splitlines())
print(prod(sum(1 for i in range(t) if i*(t-i) > r) for t, r in zip(times, records)))

time, record = int("".join(map(str, times))), int("".join(map(str, records)))
print(sum(1 for i in range(time) if i*(time-i) > record))
