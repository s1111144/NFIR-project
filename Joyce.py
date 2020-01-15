# het aanmaken van een tekstfile
# als het bestand nog niet bestaat wordt die aangemaakt

f = open("variabele.txt", "w+")

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
en = time.time()
duur = (end - start)
f.write("De duur van de scan is:" duur "seconden")

# kunnen we ervoor zorgen dat dit aan het begin van het document wordt geschreven?
# want alles wordt in volgorde geschreven


