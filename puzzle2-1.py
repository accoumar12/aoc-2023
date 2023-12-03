sum = 0

configuration = {"red": 12, "green": 13, "blue": 14}

with open("data/puzzle2.csv", "r") as f:
    for line in f:
        game_info, line = line.split(":")
        game_id = "".join(filter(str.isdigit, game_info))

        line = line.replace(",", "").replace(";", "").split()
        print(line)

        skip_iteration = False
        for i in range(len(line)):
            if line[i] in configuration:
                if int(line[i - 1]) > configuration[line[i]]:
                    skip_iteration = True

        if skip_iteration:
            continue

        sum += int(game_id)

    print(sum)
