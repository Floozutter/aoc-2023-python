from collections import Counter

card_values = {c: i for i, c in enumerate("23456789TJQKA")}
def hand_value(hand: str, joker: bool = False) -> tuple[int, tuple[int, ...]]:
    values = tuple(card_values[c] if not joker or c != "J" else -1 for c in hand)
    def hand_type(values: tuple[int, ...]) -> int:
        if -1 in values:
            i = values.index(-1)
            return max(
                hand_type(values[:i] + (v,) + values[i+1:])
                for v in card_values.values()
                if v != 9
            )
        counts = Counter(values).most_common()
        if counts[0][1] == 1:
            return 0
        elif counts[0][1] == 2 and counts[1][1] < 2:
            return 1
        elif counts[0][1] == 2 and counts[1][1] == 2:
            return 2
        elif counts[0][1] == 3 and counts[1][1] < 2:
            return 3
        elif counts[0][1] == 3 and counts[1][1] == 2:
            return 4
        elif counts[0][1] == 4:
            return 5
        else:
            return 6
    return hand_type(values), values

INPUTPATH = "input.txt"
#INPUTPATH = "input-test.txt"
with open(INPUTPATH) as ifile:
    raw = ifile.read()
pairs = tuple((l, int(r)) for l, r in map(str.split, raw.strip().splitlines()))

ranked1 = sorted(pairs, key = lambda p: hand_value(p[0]))
print(sum((i+1)*pair[1] for i, pair in enumerate(ranked1)))

ranked2 = sorted(pairs, key = lambda p: hand_value(p[0], True))
print(sum((i+1)*pair[1] for i, pair in enumerate(ranked2)))
