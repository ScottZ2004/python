import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.045)

delay_print("Hallo, ik ga je vijf keuzes geven.")
print("")
delay_print("Wat eet je meestal voor het ontbijt? BROOD, EI, CORNFLAKES of ANDERS")
print("")
antwoord_1 = input(">>> ")

if antwoord_1 == "BROOD" :
    delay_print("Jij eet dus meestal brood, dat is lekker!")
    
elif antwoord_1 == "EI" :
    delay_print("Jij eet dus meestal een eitje, dat is lekker!")

elif antwoord_1 == "CORNFLAKES" :
    delay_print("Jij eet dus meestal cornflakes, dat is lekker!")

elif antwoord_1 == "ANDERS" :
    delay_print("Jij eet dus meestal iets anders dan brood, een eitje of cornflakes")

else:
    delay_print("Je hebt niet goed antwoord gegeven. Laten we naar de volgende vraag gaan!")

print("")
delay_print("Hoeveel broers en/of zussen heb jij? Geen broer/zus is 0 en meer dan 2 is MEER.")
print("")
antwoord_2 = input(">>> ")

if antwoord_2 == "1" :
    delay_print("Jij hebt dus 1 broer/zus")
    
elif antwoord_2 == "2" :
    delay_print("Jij hebt dus 2 broer/zus")

elif antwoord_2 == "0" :
    delay_print("Jij hebt dus geen broers/zussen")

elif antwoord_2 == "MEER" :
    delay_print("Jij hebt dus MEER dan 2 broer/zus")

else:
    delay_print("Je hebt niet goed antwoord gegeven. Laten we naar de volgende vraag gaan!")

print("")
delay_print("Hoe ga jij naar je school/werk? OV of FIETS")
print("")
antwoord_3 = input(">>> ")

if antwoord_3 == "OV":
    delay_print("jij neemt het ov")

elif antwoord_3 == "FIETS":
    delay_print("jij neemt de fiets")

else:
    delay_print("Je hebt niet goed antwoord gegeven. Laten we naar de volgende vraag gaan!")
print("")
delay_print("Woon je in een STAD of in een DORP?")
print("")
antwoord_4 = input(">>> ")

if antwoord_4 == "STAD":
    delay_print("jij woont dus in een stad")

elif antwoord_4 == "DORP":
    delay_print("jij woont dus in een dorp")
else:
    delay_print("Je hebt niet goed antwoord gegeven. Laten we naar de volgende vraag gaan!")

print("")
delay_print("Nu de laatste vraag:")
print("")
delay_print("öp welke sport zit jij? VOETBAL, BASKETBAL, VOLLEYBAL, ANDERS of GEEN?")
print("")
antwoord_5 = input(">>> ")

if antwoord_5 == "VOETBAL":
    delay_print("jij zit dus op voetbal")
    
elif antwoord_5 == "BASKETBAL":
    delay_print("jij zit dus op basketbal")

elif antwoord_5 == "VOLLEYBAL":
    delay_print("jij zit dus op volleybal")

elif antwoord_5 == "ANDERS":
    delay_print("jij zit dus op op een andere sport")

elif antwoord_5 == "GEEN":
    delay_print("jij zit dus niet op een sport")

else:
    delay_print("Je hebt niet goed antwoord gegeven.")
print("")
delay_print("dit was de vragenlijst, doei")

