from collections import Counter

card_values = {c: i for i, c in enumerate("23456789TJQKA")}
def hand_value(hand: str, joker: bool = False) -> tuple[tuple[int, ...], tuple[int, ...]]:
    values = tuple(card_values[c] if not joker or c != "J" else -1 for c in hand)
    counter = Counter(values)
    if joker and (jokers := counter.pop(-1) if -1 in counter else 0):
        counter[counter.most_common(1)[0][0] if counter else -1] += jokers
    _, counts = zip(*counter.most_common())
    return tuple(counts), values

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
pairs = tuple((l, int(r)) for l, r in map(str.split, raw.strip().splitlines()))

ranked1 = sorted(pairs, key = lambda p: hand_value(p[0]))
print(sum((i+1)*pair[1] for i, pair in enumerate(ranked1)))

ranked2 = sorted(pairs, key = lambda p: hand_value(p[0], True))
print(sum((i+1)*pair[1] for i, pair in enumerate(ranked2)))
