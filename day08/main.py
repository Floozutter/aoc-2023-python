INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
instructions, tail = raw.strip().split("\n\n")
network = {l: (r[1:4], r[-4:-1]) for l, r in (line.split(" = ") for line in tail.splitlines())}

steps = 0
node = "AAA"
while node != "ZZZ":
    node = network[node][0 if instructions[steps % len(instructions)] == "L" else 1]
    steps += 1
print(steps)
