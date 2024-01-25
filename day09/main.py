def predict(history: tuple[int, ...]) -> tuple[int, int]:
    if all(z == 0 for z in history):
        return 0, 0
    ldiff, rdiff = predict(tuple(b - a for a, b in zip(history, history[1:])))
    return history[0] - ldiff, history[-1] + rdiff

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
histories = tuple(tuple(map(int, line.split())) for line in raw.strip().splitlines())

lsum, rsum = map(sum, zip(*map(predict, histories)))
print(rsum)
print(lsum)
