race = [48876981, 255128811171623]

product = 1

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
