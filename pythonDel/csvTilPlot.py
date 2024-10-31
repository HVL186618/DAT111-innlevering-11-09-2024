"""
Dette er ett av to skjelettprogram for Python-delen av semesteroppgaven i DAT111 H2024.

Fullfør denne filen basert på kravene og strukturen spesifisert her og i pdf-filen på Canvas.

Merk: indenteringen som er brukt på kommentarene indikerer hvilket nivå koden dere fyller inn skal ligge på.

Fyll inn informasjonen under.
Gruppe:
    
Navn på gruppemedlemmer:
    
"""

### Importerer nødvendige bibliotek ###
import csv
# 'as' oppretter et alias på høyre siden (plt) som vi kan bruke i stedet for det fulle navnet på venstresiden.
import matplotlib.pyplot as plt 

### Funksjon som styrer flyten i programmet ###
def main():
    # Bruk importerBesoekertall-funksjonen til å opprette en liste bestående av alle radene
    # i csv-filen og lagre denne i en variabel.
    csvliste = importerBesoekertall()
    
    # Henter ut timene Læringslab er åpent fra csvliste, konverterer verdiene til heltall og gjør de om til en liste.
    # Fyll inn korrekte verdier i hakeparentesene for å hente ut de korrekte verdiene fra header-raden. Bruk slicing
    # som dere kan lese mer om her: https://www.pythonmorsels.com/slicing/
    x = list(map(int,csvliste[0][1:]))  # x = list(map(int,csvliste[???][???]))

    # Gå gjennom alle radene i csvliste, hent ut verdier, finn anbefalte tidsrom og plot grafer.
    # Legg inn korrekt verdi i hakeparentesene.
    for rad in csvliste[1:]:
        dag = rad[0]
        y = list(map(int,rad[1:]))
        
        # Utfør et kall på anbefalteTidsrom-funksjonen med følgende argument: dag, liste over tidspunkt, 
        # liste over besøkende og grenseverdi.
        anbefalteTidsrom(dag, x, y, 5)
        
        # Utfør et kall på plotGraf-funksjonen med verdiene for x- og y-aksen som argument, samt navnet på dagen.
        plotGraf(x, y, dag)

### Funksjon som importerer fil ved hjelp av csv-biblioteket ###
def importerBesoekertall(filnavn="besoekerstatistikk.csv"):
    rows = []

    with open(filnavn, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            rows.append(row)
    return rows

### Funksjon som plotter en graf ved hjelp av matplotlib ###
def plotGraf(x, y, navn):
    
    # Opprett fire grenseverdier som spesifiserer lite, medium, høyt og veldig høyt besøkstall.
    li, me, hi, vh = 5, 10, 15, 20
    
    # Spesifiserer fargene i plottet. Vi bruker listekomprehering som setter verdier basert på elementene i listen,
    # dvs. vi går gjennom alle verdiene i listen og setter de til en ny verdi basert på sannhetsuttrykk.
    # Det fungerer likt som om vi hadde gjort det med for-else-struktur, men litt mer kompakt.
    # Vi opererer med RGBA-verdier, derfor trenger vi "True" som tillegsverdi i hakeparentes.
    barcolor =  [
        {
            verdi < li: 'green', li <= verdi < me: 'yellow',
            me  <= verdi < hi: 'orange', hi  <= verdi <= vh: 'red'
        }[True]
        for verdi in y
    ]
    
    # Definerer barene i plottet.
    # Bruk matplotlib.pyplot sin bar-funksjon. Spesifiser bredde på barene, kantfarge, linjebredde og 
    # farger (som vi nettopp har lagret i en liste).
    plt.bar(x, y, color=barcolor, edgecolor='black', linewidth=1)
    
    # Legger til navn på x- og y-aksene, samt tittel på grafen.
    # Bruk matplotlib.pyplot sin xlabel-, ylabel- og title-funksjon.
    plt.title(f"Besøkstall: {navn}")
    plt.xlabel("Tidsrom")
    plt.ylabel("Besøkstall")
    
    # Lagrer plottet.
    # Kall på matplotlib.pyplot sin savefig-funksjon med korrekt navn på grafen som argument.
    # FYLL INN KODE HER #
    
    # Viser plottet i IDE.
    # Merk: om vi ikke hadde gjort dette måtte vi ha husket å lukke plottet, noe som er innebygget i show-funksjonen.
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
    # Oppretter variabler for å holde på tidsrom og for å mellomlagre start- og sluttverdi for tidsrom.
    # Bruk verdien 0 som initiell verdi for start- og sluttverdi og for å indikere at verdiene ikke har blitt satt enda.
    # FYLL INN KODE HER #
    
    # Går gjennom alle tidspunktene og tilhørende besøkstall for å sjekke om de er del av et anbefalt tidsrom.
    # Siden vi går gjennom to lister bruker vi en teller/indeks. Antall gjennomkjøringer kan spesifiseres ved
    # å bruke len-funksjonen på listen som skal itereres over for å få lengden på listen, for deretter å bruke
    # dette som argument til range-funksjonen for å lage en sekvens med tall.
    # FYLL INN KODE HER #
        
        # Henter ut tidspunkt og tilhørende antall besøkende og lagrer det i variabler.
        # Husk å bruke indeks for å gjøre dette.
        # FYLL INN KODE HER #
        
        # Sjekker om et nytt anbefalt tidsrom er startet ved å sjekke om antall besøkende er under grenseverdien.
        # FYLL INN KODE HER #
            
            # Sjekker om startpunkt for tidsrommet ikke er satt.
            # Dette gjør vi for å håndtere tidsrom som er lengre enn en time.
            # FYLL INN KODE HER #
                
                # Setter vi startpunkt til gjeldende tidspunkt.
                # FYLL INN KODE HER #
                
            # Oppdaterer sluttpunktet for tidsrommet til å være gjeldende tidspunkt.
            # FYLL INN KODE HER #
            
            # Sjekker om vi er på enden av listen eller neste element er større enn grenseverdien 
            # FYLL INN KODE HER #
            
                # Tidsrommet legges til i listen og tidspunktvariablene tilbakestilles til 0.
                # FYLL INN KODE HER #
    
    
    # Skriver ut de anbefalte tidsrommene.
    # Skriver først ut en innledende melding som beskriver hva som blir skrevet ut
    # FYLL INN KODE HER #
    
    # Går gjennom alle tidene i tidsrommet
    # FYLL INN KODE HER #
        
        # Dersom tidsrommet består av en time, dvs. start og slutt er like, skrives det ut på egnet format.
        # FYLL INN KODE HER #
        
        # Dersom tidsrommet består av flere timer skrives det ut med bindestrek mellom.
        # FYLL INN KODE HER #

    # Skriver ut en tom linje for å få penere formattering i utskriften.
    # FYLL INN KODE HER #    
            
    # Returner tidsrommet
    # FYLL INN KODE HER #

# Kaller på main-metoden til slutt. Siden Python er et tolket språk må alle funksjoner som brukes i 
# en funksjon allerede være definert når den kalles. Dette er en av måtene å håndtere dette på.
# FYLL INN KODE HER #
if __name__ == "__main__":
    main()