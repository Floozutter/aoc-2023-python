from math import lcm

INPUTPATH = "input.txt"
#INPUTPATH = "input-test1.txt"
#INPUTPATH = "input-test2.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
head, tail = raw.strip().split("\n\n")
instruction = lambda step: head[step % len(head)] == "R"
network = {l: (r[1:4], r[-4:-1]) for l, r in (line.split(" = ") for line in tail.splitlines())}

def steps(start: str) -> int:
    i, node = 0, start
    while node[-1] != "Z":
        i, node = i+1, network[node][instruction(i)]
    return i

print(steps("AAA"))
print(lcm(*(steps(node) for node in network if node[-1] == "A")))
