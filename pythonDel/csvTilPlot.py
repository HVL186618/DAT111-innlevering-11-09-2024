"""
Dette er ett av to skjelettprogram for Python-delen av semesteroppgaven i DAT111 H2024.

Fullfør denne filen basert på kravene og strukturen spesifisert her og i pdf-filen på Canvas.

Merk: indenteringen som er brukt på kommentarene indikerer hvilket nivå koden dere fyller inn skal ligge på.

Fyll inn informasjonen under.
Gruppe:
    
Navn på gruppemedlemmer:
    
"""

import csv
import matplotlib.pyplot as plt 

def main():
    csvliste = importerBesoekertall()
    x = list(map(int,csvliste[0][1:]))  # x = list(map(int,csvliste[???][???]))

    for rad in csvliste[1:]:
        dag = rad[0]
        y = list(map(int,rad[1:]))

        anbefalteTidsrom(dag, x, y, 7)

        plotGraf(x, y, dag)

def importerBesoekertall(filnavn="besoekerstatistikk.csv"):
    rows = []

    with open(filnavn, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            rows.append(row)
    return rows

def plotGraf(x, y, navn):
    li, me, hi, vh = 5, 10, 15, 20
    barcolor =  [
        {
            verdi < li: 'green', li <= verdi < me: 'yellow',
            me  <= verdi < hi: 'orange', hi  <= verdi <= vh: 'red'
        }[True]
        for verdi in y
    ]
    plt.bar(x, y, color=barcolor, edgecolor='black', linewidth=1)
    plt.title(f"Besøkstall: {navn}")
    plt.xlabel("Tidsrom")
    plt.ylabel("Besøkstall")
    plt.show()



### Funksjon som finner og skriver ut anbefalte tidsrom for besøk. ###
def anbefalteTidsrom(dag, tidspunktliste, besoekendeliste, grenseverdi):
    tidsrom = []
    start = 0
    slutt = 0

    for i in range(len(tidspunktliste)):
        tidspunkt = tidspunktliste[i]
        antall_besoekende = besoekendeliste[i]

        if antall_besoekende < grenseverdi:
            if start == 0:
                start = tidspunkt
            slutt = tidspunkt

            if i == len(tidspunktliste) - 1 or besoekendeliste[i + 1] >= grenseverdi:
                tidsrom.append((start, slutt))
                start = 0
                slutt = 0

    print(f"Anbefalte tidsrom å besøke Læringslab på {dag}:")
    for start, slutt in tidsrom:
        if start == slutt:
            print(f"Kl. {start}:00")
        else:
            print(f"Kl. {start}:00 - {slutt}:00")
    print()

    return tidsrom
if __name__ == "__main__":
    main()