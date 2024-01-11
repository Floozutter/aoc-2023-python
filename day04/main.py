INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()

wincounts = tuple(
    len(set(l.split()) & set(r.split()))
    for l, r in (line.split(": ")[1].split(" | ") for line in raw.strip().splitlines())
)
print(sum(int(2**(n-1)) for n in wincounts))

scratchcards = [1] * len(wincounts)
for i, n in enumerate(wincounts):
    for j in range(i+1, i+1+n):
        scratchcards[j] += scratchcards[i]
print(sum(scratchcards))
