letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

def classify(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts: return 6
    if 4 in counts: return 5 
    if 3 in counts:
        if 2 in counts: return 4
        return 3
    if counts.count(2) == 4: return 2
    if 2 in counts: return 1
    return 0

def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])

with open('input.txt', 'r') as input:
    plays = [(line.split()[0], int(line.split()[1])) for line in input.read().splitlines()]
    plays.sort(key=lambda play: strength(play[0]))
    total = 0

    for rank, (hand, bid) in enumerate(plays, 1):
        total += rank * bid
    # print(plays)
    print(total)