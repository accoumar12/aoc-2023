sum = 0

with open("data/puzzle2.csv", "r") as f:
    for line in f:
        power = 1
        minimum_set = {"red": 0, "green": 0, "blue": 0}
        _, line = line.split(":")

        line = line.replace(",", "").replace(";", "").split()
        print(line)

        for i in range(len(line)):
            if line[i] in minimum_set.keys():
                if int(line[i - 1]) > minimum_set[line[i]]:
                    minimum_set[line[i]] = int(line[i - 1])
        print(minimum_set)
        for color in minimum_set:
            power *= minimum_set[color]
        sum += power

    print(f"The sum is {sum}")
