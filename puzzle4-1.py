sum = 0

with open("data/puzzle4.csv", "r") as file:
    for line in file:
        print(line)
        line = line.split(":")[1]

        card, numbers = line.split("|")
        card, numbers = card.split(), numbers.split()

        card = [int(x) for x in card]
        numbers = [int(x) for x in numbers]

        power = -1

        for number in numbers:
            for card_number in card:
                if card_number == number:
                    power += 1
                    break

        if power == -1:
            continue
        else:
            sum += 2**power
print(sum)
