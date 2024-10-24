import csv
import random


with open('besoekerstatistikk.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Dag"] + [str(i) for i in range(9, 19)])
    for dag in "mandag tirsdag onsdag torsdag fredag".title().split(" "):
        writer.writerow(
            [dag] + \
            [random.randint(0, 5 + i * 3) for i in range(3)] + \
            [random.randint(5, 20) for i in range(4)] + \
            [random.randint(0, 11 - i * 4) for i in range(2)]
        )
