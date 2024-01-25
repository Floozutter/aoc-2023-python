def predict(history: tuple[int, ...]) -> int:
    if all(z == 0 for z in history):
        return 0
    diffs = tuple(b - a for a, b in zip(history, history[1:]))
    return history[-1] + predict(diffs)

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
histories = tuple(tuple(map(int, line.split())) for line in raw.strip().splitlines())

print(sum(map(predict, histories)))
