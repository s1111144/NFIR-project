# het aanmaken van een tekstfile
# als het bestand nog niet bestaat wordt die aangemaakt

found_naam = 'found.txt'
found = open(found_naam, "w+")


not_found_naam = 'not_found.txt'
not_found = open(not_found_naam, "w+")

# variabele moet waarde found of not found krijgen

if een van de ioc's is found
    variabele = "found"

else variabele = "not found"



# bij elke ioc moet naar de textfile geschreven worden

if IOC 1 is found: # als de uitkomst positief is
    f.write("IOC 1: found")

    else f.write("IOC 1: not found") # als de uitkomst negatief is

f.close()


# datum en tijd

import datetime

datum = datetime.datetime.now()

f.write(datum)


# duur van de scan

import time

start = time.time()
end = time.time()
duur = (end - start)
f.write("De duur van de scan is:" duur "seconden")

# kunnen we ervoor zorgen dat dit aan het begin van het document wordt geschreven?
# want alles wordt in volgorde geschreven


