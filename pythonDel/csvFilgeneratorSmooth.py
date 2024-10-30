import csv
import random

# for mer naturlig statistikk, gjør beregingen i csvFilegeneratorSimple {n} ganger

n = 10
dager = "mandag tirsdag onsdag torsdag fredag".title().split(" ")
tidspunkter = [str(i) for i in range(9, 19)]
summer = {dag: [0] * len(tidspunkter) for dag in dager}

for _ in range(n):
    for dag in dager:
        # Generer tilfeldige verdier for alle tidspunktene i løpet av dagen.
        verdier = (
                [random.randint(0, 6 + i * 5) for i in range(3)] +
                [random.randint(10 + i * 2, 20) for i in range(2)] +
                [random.randint(10 - i * 5, 20 - i) for i in range(2)] +
                [random.randint(0, 11 - i * 4) for i in range(3)]
        )

        for i, verdi in enumerate(verdier):
            summer[dag][i] += verdi

with open('besoekerstatistikk.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Dag"] + tidspunkter)
    for dag in dager:
        gjennomsnitt = [round(total / n) for total in summer[dag]]
        writer.writerow([dag] + gjennomsnitt)
