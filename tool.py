import hashlib, os, sys
import winreg
import socket
import time
from datetime import datetime
now = datetime.now()
myhost = socket.gethostname()

#Robin
def registry():
    start = time.time()
    try:
        with open('reg_invoer.txt', 'r') as inlezen:                            #Deze functie is bedoelt voor het splitsen van de ingevoerde sleutels in een tweetal lijsten. Deze sleutels worden uitgelezen uit het tekstbestand "reg_invoer.txt"
            sleutels = inlezen.readlines()                                      #Het eerste deel is het basispd van de te onderzoeken sleutel, het tweede deel de specifieke map of sleutel in dit pad
            hkey_lijst = [k.split()[0] for k in sleutels]                       #Vervolgend worden de lijsten met elkaar vergeleken in de vorm van een if statement in een while loop, die net zo vaak loopt als het aantal aanwezige entries.
            path_lijst = [p.split()[1] for p in sleutels]

        x = 0
        y = 0
        z = len(hkey_lijst)
        counter = 0

        while counter <= z:
            hkey = hkey_lijst[x]
            path = path_lijst[y]
            x += 1
            y += 1
#/Robin
#Alex
            try:
                # alle registerpaden welke zijn ingevoerd door de gebruiker tijdens de configuratie zijn nu opgesplitst en geloopt
                # allereerst wordt gekeken naar het basispad (HKEY_*) en zodra deze gevonden is zal de rest van het registerpad opgezocht worden
                # indien het volledige registerpad is gevonden zal dit weggeschreven worden naar een tekstbestand en staat daarbij het volgende: + Found (tijdstip)
                # in het geval dat een registerpad niet is gevonden zal dit ook weggeschreven worden en staat daarbij het volgende: - Not Found (tijdstip)
                # de tekst '+' is in dit geval een hulpmiddel om er later voor te zorgen dat de naam van het tekstbestand gemakkelijk kan worden aangepast naar Found/Not Found 
                if hkey == 'HKEY_CLASSES_ROOT':
                    datum = now.strftime("%d/%m/%Y %H:%M:%S")
                    reg = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + '\\' + path + '\n + Found ' + datum + '\n\n')
                        file_out.close()
                    winreg.CloseKey(reg)

                elif hkey == 'HKEY_CURRENT_USER':
                    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + '\\' + path + '\n + Found ' + datum + '\n\n')
                        file_out.close()
                    winreg.CloseKey(reg)
                
                elif hkey == 'HKEY_LOCAL_MACHINE':
                    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + '\\' + path + '\n + Found ' + datum + '\n\n')
                        file_out.close()
                    winreg.CloseKey(reg)

                elif hkey == 'HKEY_USERS':
                    reg = winreg.OpenKey(winreg.HKEY_USERS, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + '\\' + path + '\n + Found ' + datum + '\n\n')
                        file_out.close()
                    winreg.CloseKey(reg)

                elif hkey == 'HKEY_CURRENT_CONFIG':
                    reg = winreg.OpenKey(winreg.HKEY_CURRENT_CONFIG, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + '\\' + path + '\n + Found ' + datum + '\n\n')
                        file_out.close()
                    winreg.CloseKey(reg)
            except:
                with open('reg_found.txt', 'a+') as file_out:
                    file_out.write(hkey + '\\' + path + '\n - Not Found ' + datum + '\n\n')
                    file_out.close()
    except:
        pass
#/Alex
#Joyce  
    end = time.time()
    duur = (end - start)
    duur = ("%.2f" % duur)

    with open("reg_found.txt", "a") as file_out:
        file_out.write("De duur van de scan is: " + str(duur))
        file_out.close()

    with open("reg_found.txt", "r") as file_out:
        if '+' in file_out.read():
            naam = 1
            file_out.close()        
        else:
            naam = 0
            file_out.close()

    if naam == 1:
        os.rename("reg_found.txt", "Found - Registry Log [" + myhost + "].txt")

    elif naam == 0:
        os.rename("reg_found.txt", "Not Found - Registry Log [" + myhost + "].txt")
#Joyce

def file():
    print('def file')

def main():
    registry()
    file()
    
if __name__=='__main__':
    main()
