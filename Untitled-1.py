#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:18:34 2024

@author: tord
"""

# Karaktervariabler
navnPaaKarakter = input("Hva er navnet på karakteren?\n")
gull = 100

utstyrnavn1 = "Ingenting"
utstyrnavn2 = "Ingenting"
utstyrnavn3 = "Ingenting"

utstyrverdi1 = 0
utstyrverdi2 = 0
utstyrverdi3 = 0

# Butikkvariabler
sverdverdi = 20
stavverdi = 70
kappeverdi = 25

# Gir utskrift til brukeren for å starte karakterskaperen
print("\nDu skal nå kjøpe startutstyr fra butikken.")
print("Butikken består av følgende varer:")
print("Vare 1: sverdverdi - verdi: " + str(sverdverdi))
print("Vare 2: stavverdi - verdi:", stavverdi)
print("Vare 3: kappeverdi - verdi: " + str(kappeverdi) + "/n")

# Håndterer kjøp av første utstyr
oensketVare1 = input("Hvilket varenummer ønsker du å kjøpe (1-3)? ")
if(oensketVare1 == "1" and gull > sverdverdi):
    utstyrnavn1 = "Sverd"
    utstyrverdi1 = sverdverdi
    gull -= sverdverdi
elif(oensketVare1 == "2" and gull > stavverdi):
    utstyrnavn1 = "Stav"
    utstyrverdi1 = stavverdi
    gull -= stavverdi
elif(oensketVare1 == "3" and gull > kappeverdi):
    utstyrnavn1 = "Kappe"
    utstyrverdi1 = kappeverdi
    gull -= kappeverdi
else:
    print("Ukjent vare, eller ikke råd til vare. Ingenting ble kjøpt.")
    
# Håndterer kjøp av andre utstyr
oensketVare2 = input("Hvilket varenummer ønsker du å kjøpe (1-3)? ")
if(oensketVare2 == "1" and gull > sverdverdi):
    utstyrnavn2 = "Sverd"
    utstyrverdi2 = sverdverdi
    gull -= sverdverdi
elif(oensketVare2 == "2" and gull > stavverdi):
    utstyrnavn2 = "Stav"
    utstyrverdi2 = stavverdi
    gull -= stavverdi
elif(oensketVare2 == "3" and gull > kappeverdi):
    utstyrnavn2 = "Kappe"
    utstyrverdi2 = kappeverdi
    gull -= kappeverdi
else:
    print("Ukjent vare, eller ikke råd til vare. Ingenting ble kjøpt.")

# Håndterer kjøp av tredje utstyr
oensketVare3 = input("Hvilket varenummer ønsker du å kjøpe (1-3)? ")
if(oensketVare3 == "1" and gull > sverdverdi):
    utstyrnavn3 = "Sverd"
    utstyrverdi3 = sverdverdi
    gull -= sverdverdi
elif(oensketVare3 == "2" and gull > stavverdi):
    utstyrnavn3 = "Stav"
    utstyrverdi3 = stavverdi
    gull -= stavverdi
elif(oensketVare3 == "3" and gull > kappeverdi):
    utstyrnavn3 = "Kappe"
    utstyrverdi3 = kappeverdi
    gull -= kappeverdi
else:
    print("Ukjent vare, eller ikke råd til vare. Ingenting ble kjøpt.")

# Gir en utskrift av karakterinfo
print("\nKarakteren er nå ferdigskapt og har følgende detaljer:")
print("Navn: " + navnPaaKarakter);
print("Utstyr 1: " + utstyrnavn1 + ", med verdi", utstyrverdi1)
print("Utstyr 2: " + utstyrnavn2 + ", med verdi", utstyrverdi2)
print("Utstyr 3: " + utstyrnavn3 + ", med verdi", utstyrverdi3)