from collections import Counter

card_values = {c: i for i, c in enumerate("23456789TJQKA")}
def hand_value(hand: str) -> tuple[int, tuple[int, int, int, int, int]]:
    values = tuple(card_values[c] for c in hand)
    counts = Counter(values).most_common()
    if counts[0][1] == 1:
        return 0, values
    elif counts[0][1] == 2 and counts[1][1] < 2:
        return 1, values
    elif counts[0][1] == 2 and counts[1][1] == 2:
        return 2, values
    elif counts[0][1] == 3 and counts[1][1] < 2:
        return 3, values
    elif counts[0][1] == 3 and counts[1][1] == 2:
        return 4, values
    elif counts[0][1] == 4:
        return 5, values
    else:
        return 6, values

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
pairs = tuple((l, int(r)) for l, r in map(str.split, raw.strip().splitlines()))

ranked = sorted(pairs, key = lambda p: hand_value(p[0]))
print(sum((i+1)*pair[1] for i, pair in enumerate(ranked)))
