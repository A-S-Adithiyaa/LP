'''
The Birthday Paradox, also called the
Birthday Problem, is the surprisingly high
probability that two people will have the
same birthday even in a small group of people.
In a group of 70 people, there is a 99.9 percent chance
of two people having a matching birthday. But even
in a group as small as 23 people, there is a 50 percent
chance of a matching birthday. This program performs several probability experiments to determine
the percentages for groups of different sizes. We call these types of experiments, in which we conduct multiple random trials to understand the
likely outcomes, Monte Carlo experiments.
'''


import random


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days = list(map(str, range(1, 32)))

n = int(input("Enter the number of people : "))
number_of_reps = int(input("Enter the number of times this has to be repeated : "))
matching = 0


for count in range(number_of_reps):
    if count in [250, 500, 1000, 2000, 4000, 6000, 8000, 10000]:
        print("Reached", count, "count...")

    birthdays = {}

    for i in range(n):
        date = random.choice(months) + random.choice(days)
        while date in ['Feb30', 'Feb31']:
            date = random.choice(months) + random.choice(days)

        if date not in birthdays:
            birthdays[date] = 1
        else:
            birthdays[date] += 1

    if max(list(birthdays.values())) > 1:
        matching += 1

prob = matching*100/count
print(str(prob) + "%")
