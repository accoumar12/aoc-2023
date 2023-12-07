from collections import Counter
from functools import cmp_to_key

mapping = {f"{i}": i for i in range(2, 10)} | {
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}

with open("data/puzzle7.csv") as file:
    lines = file.readlines()

game = [line.split() for line in lines]

hands = [[], [], [], [], [], [], []]


def is_stronger(hand1, hand2):
    for i in range(len(hand1[0])):
        if mapping[hand1[0][i]] > mapping[hand2[0][i]]:
            return 1
        elif mapping[hand1[0][i]] < mapping[hand2[0][i]]:
            return -1
    return 0


def find_index_with_joker(hand):
    best_index = 0
    initial_hand = hand
    for key in mapping:
        hand = initial_hand.replace("J", key)
        index = find_index(hand)
        if index > best_index:
            best_index = index
    return best_index


def find_index(hand):
    length = len(hand)
    length_distinct = len(set(hand))
    if length_distinct == length:
        index = 0
    elif length_distinct == length - 1:
        index = 1
    elif length_distinct == 1:
        index = 6
    elif length_distinct == 2:
        counter = Counter(hand)
        index = 5
        for _, value in counter.items():
            if value == 2:
                index = 4
    else:
        counter = Counter(hand)
        index = 2
        for _, value in counter.items():
            if value == 3:
                index = 3
    return index


for i in range(len(game)):
    index = find_index_with_joker(game[i][0])
    hands[index].append(game[i])

for i in range(len(hands)):
    hands[i] = sorted(hands[i], key=cmp_to_key(is_stronger))

concatenated_hands = []

for i in range(len(hands)):
    for j in range(len(hands[i])):
        concatenated_hands.append(hands[i][j])

print(concatenated_hands)

total = 0

for i in range(len(concatenated_hands)):
    total += int(concatenated_hands[i][1]) * (i + 1)

print(total)
