somme = 0

file_path = "data/puzzle1.csv"
matches = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open(file_path) as f:
    with open("data/puzzle1-test.csv", "w") as new_f:
        for line in f:
            for i in range(0, len(line)):
                for j in range(2, 6):
                    if line[i : i + j] in matches:
                        line = line.replace(line[i : i + j], matches[line[i : i + j]])
                        break
            # for i in range(len(line), -1, -1):
            #     for j in range(2, 4):
            #         if line[i - j : i] in matches:
            #             line = line.replace(line[i - j : i], matches[line[i - j : i]])
            #             break
            for letter in line:
                if letter.isdigit():
                    premier = letter
                    break
            for letter in line[::-1]:
                if letter.isdigit():
                    dernier = letter
                    break
            nombre = int(premier + dernier)
            somme += nombre
            new_f.write(line)
print(somme)
