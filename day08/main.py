INPUTPATH = "input.txt"
#INPUTPATH = "input-test1.txt"
#INPUTPATH = "input-test2.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
instructions, tail = raw.strip().split("\n\n")
network = {l: (r[1:4], r[-4:-1]) for l, r in (line.split(" = ") for line in tail.splitlines())}

i = 0
node = "AAA"
while node != "ZZZ":
    node = network[node][0 if instructions[i%len(instructions)] == "L" else 1]
    i += 1
print(i)

j = 0
nodes = tuple(n for n in network if n[-1] == "A")
while any(n[-1] != "Z" for n in nodes):
    nodes = tuple(network[n][0 if instructions[j%len(instructions)] == "L" else 1] for n in nodes)
    j += 1
print(j)
