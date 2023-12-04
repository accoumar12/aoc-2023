file = open("data/puzzle4.csv").readlines()

total = 0
cards = [1 for _ in file]

for index, line in enumerate(file):
    line = line.split(":")[1]
    line, numbers = line.split("|")
    possibilities, numbers = line.split(), numbers.split()

    number_of_common_elements = len(set(possibilities) & set(numbers))

    if number_of_common_elements > 0:
        total += 2 ** (number_of_common_elements - 1)

    for i in range(number_of_common_elements):
        cards[index + i + 1] += cards[index]

print(total, sum(cards))
