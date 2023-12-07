races = [[48, 255], [87, 1288], [69, 1117], [81, 1623]]

product = 1

for race in races:
    time_hold = 1
    while time_hold * (race[0] - time_hold) < race[1]:
        time_hold += 1

    first_time = time_hold

    time_hold = race[0] - 1
    while time_hold * (race[0] - time_hold) < race[1]:
        time_hold -= 1

    second_time = time_hold

    number_of_ways = second_time - first_time + 1

    product *= number_of_ways
print(product)
