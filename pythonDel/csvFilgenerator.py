"""
Dette er ett av to skjelettprogram for Python-delen av semesteroppgaven i DAT111 H2024.

Fullfør denne filen basert på kravene og strukturen spesifisert her og i pdf-filen på Canvas.

Merk: indenteringen som er brukt på kommentarene indikerer hvilket nivå koden dere fyller inn skal ligge på.

Fyll inn informasjonen under.
Gruppe:
    
Navn på gruppemedlemmer:
    
"""

### Importer nødvendige bibliotek ###
import csv
import random
import os

### Generer csv-fil med csv-biblioteket ###
# Åpne eksisterende fil/opprett ny med det spesifiserte navnet, i skrivemodus.
with open('besoekerstatistikk.csv', 'w', newline='') as file:
    # Opprett en referanse til csv-biblioteket sin skriverfunksjon med den åpnede filen som argument.
    writer = csv.writer(file)
    
    # Lag header-raden som skal bestå av tekststrengen "Dag" og alle tidspunktene i åpningstiden.
    writer.writerow(["Dag"] + [str(i) for i in range(9, 19)])
    for dag in "mandag tirsdag onsdag torsdag fredag".title().split(" "):
        writer.writerow(
            [dag] + \
            [random.randint(0, 5 + i * 3) for i in range(3)] + \
            [random.randint(5, 20) for i in range(4)] + \
            [random.randint(0, 11 - i * 4) for i in range(2)])

    
    # Skriv header-raden til filen ved hjelp av skriverfunksjonen.

    
    # Lag en liste av alle dagene det er åpent på Læringslab.
    # FYLL INN KODE HER #
    
    # Vi skal nå generere besøkstall per dag, med tilfeldig variasjon, og skrive de til fil.
    # Bruk en for-løkke til å gå gjennom alle dagene i listen over dager.
    # FYLL INN KODE HER #
        
        # Opprett en ny liste som skal representere dagens besøkstall.
        # Legg inn navnet på dagen som startelement.
        # FYLL INN KODE HER #

        # Opprett to variabler som holder på start- og sluttverdi for det tilfeldige intervallet.
        # FYLL INN KODE HER #
        
        # Bruk en for-løkke til å gå gjennom alle tidspunktene i åpningstiden ved hjelp av range()-funksjonen.
        # FYLL INN KODE HER #
            
            # Opprett en tilfeldig verdi ved hjelp av random.sample(). Som argument til funksjonen
            # gir dere range() med start- og slutt-verdier som dere har lagret i variabler tidligere.
            # random.sample() returnerer en liste (i dette tilfellet av størrelse 1), hent ut den
            # første verdien fra listen.
            # FYLL INN KODE HER #
        
            # Legg til den nye verdien i listen for dagens besøkstall.
            # FYLL INN KODE HER #
            
            # Bruk en if-elif-else-struktur for å endre på start- og sluttverdi for det tilfeldige intervallet.
            # Målet er at det skal resultere i en naturlig fordeling av besøkende, for eksempel normalfordelt eller
            # med en topp før og en etter lunsjtid.
            # FYLL INN KODE HER #
        
        # Skriv raden til fil.
        # FYLL INN KODE HER #