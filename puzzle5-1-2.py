# The results of both questions were found with this code... the second one was found thanks to binary search

with open("data/puzzle5.csv") as file:
    line = file.readline()
    seeds = [int(x) for x in line.split(":")[1].split()]

    mappings = []
    line = file.readline()
    line = file.readline()
    line = file.readline()
    for i in range(7):
        mapping = []
        while line.split():
            mapping_item = line.split()
            mapping_item = [int(x) for x in mapping_item]
            mapping.append(mapping_item)
            line = file.readline()
        mappings.append(mapping)
        line = file.readline()
        line = file.readline()

    # print(mappings)
    lowest = float("inf")

    for seed in seeds:
        current = seed
        for i in range(len(mappings)):
            for j in range(len(mappings[i])):
                if not (
                    mappings[i][j][1]
                    <= current
                    <= mappings[i][j][1] + mappings[i][j][2]
                ):
                    continue
                else:
                    current = mappings[i][j][0] + current - mappings[i][j][1]
                    break
        if current < lowest:
            lowest = current
            print(lowest)
    print(lowest)
