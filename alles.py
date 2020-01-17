import hashlib, os, sys
import winreg
import datetime
filename = datetime.datetime.now()

def kiezen_optie():
    print('U heeft de mogelijkheid te kiezen uit:\n 1. Registry Checker\n 2. File Checker')
    while True:
        scankeuze = input('Welke van de opties wilt u kiezen? Voer de cijferwaarde in: ')
        if scankeuze == '1':
            scankeuze = 'Registry'
            break
        elif scankeuze == '2':
            scankeuze = 'File'
            break
        else:
            print('waarde niet bekend, probeer het opnieuw') 
    return scankeuze

def Opstellen_pad(scankeuze):
    if scankeuze == 'Registry':
        print('U heeft gekozen voor de Registry Checker.\nDe mogelijkheden voor het scannen in de basispaden zijn:\n1. HKEY_CLASSES_ROOT\n2. HKEY_CURRENT_USER\n3. HKEY_LOCAL_MACHINE\n4. HKEY_USERS\n5. HKEY_CURRENT_CONFIG')
        while True:
            basispad = input('Welk van bovenstaande basispaden wilt u gebruiken? Voer aub de cijferwaarde in: ')
            if basispad == '1':
                basispad = 'HKEY_CLASSES_ROOT'
                break
            elif basispad == '2':
                basispad = 'HKEY_CURRENT_USER'
                break
            elif basispad == '3':
                basispad = 'HKEY_LOCAL_MACHINE'
                break
            elif basispad == '4':
                basispad = 'HKEY_USERS'
                break
            elif basispad == '5':
                basispad = 'HKEY_CURRENT_CONFIG'
                break
            else:
                print('waarde niet bekend, probeer het opnieuw')
        return basispad

def Opstellen_sleutel(scankeuze):
    if scankeuze == 'Registry':
        while True:
            sleutel = input('Welke map/sleutel wilt u zoeken?: ')
            bevestiging_sleutel = input('Is dit de juiste map/sleutel?: ' + sleutel + '\nGelieve te bevestigen in de vorm "ja" of "nee": ')
            if bevestiging_sleutel == 'ja':
                break
            elif bevestiging_sleutel == 'nee':
                print('Voer opnieuw uw waarde in, aub')
            else:
                print('Dit is een verplicht veld, wilt u deze invullen aub')
        return sleutel

# vanaf hier moet de .exe aangemaakt worden
# pas wanneer de .exe wordt uitgevoerd moet onderstaande code uitgevoerd worden
      
def Register_IOC1(scankeuze, basispad, sleutel):
    if scankeuze == 'Registry':
        try:
            reg_check = ''
            print('Het door u gekozen pad is: ' + basispad + '\\' + sleutel)
            if basispad == 'HKEY_CLASSES_ROOT':
                reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
                key = winreg.OpenKey(reg, sleutel)
                print(sleutel + " found.")
                reg_check = 1
                if reg_check == 1:
                    found_naam = 'found123.txt'
                    found = open(found_naam, "w+")
                    found.write("IOC 1: found in het door u gekozen pad: " + basispad + '\\' + sleutel)
                winreg.CloseKey(key)
            elif basispad == 'HKEY_CURRENT_USER':
                reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                key = winreg.OpenKey(reg, sleutel)
                print(sleutel + " found.")
                reg_check = 1
                if reg_check == 1:
                    found_naam = 'found123.txt'
                    found = open(found_naam, "w+")
                    found.write("IOC 1: found in het door u gekozen pad: " + basispad + '\\' + sleutel)
                winreg.CloseKey(key)
            elif basispad == 'HKEY_LOCAL_MACHINE':
                reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
                key = winreg.OpenKey(reg, sleutel)
                print(sleutel + " found.")
                reg_check = 1
                if reg_check == 1:
                    found_naam = 'found123.txt'
                    found = open(found_naam, "w+")
                    found.write("IOC 1: found in het door u gekozen pad: " + basispad + '\\' + sleutel)
                winreg.CloseKey(key)
            elif basispad == 'HKEY_USERS':
                reg = winreg.ConnectRegistry(None, winreg.HKEY_USERS)
                key = winreg.OpenKey(reg, sleutel)
                print(sleutel + " found.")
                reg_check = 1
                if reg_check == 1:
                    found_naam = 'found123.txt'
                    found = open(found_naam, "w+")
                    found.write("IOC 1: found in het door u gekozen pad: " + basispad + '\\' + sleutel)
                winreg.CloseKey(key)
            elif basispad == 'HKEY_CURRENT_CONFIG':
                reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_CONFIG)
                key = winreg.OpenKey(reg, sleutel)
                print(sleutel + " found.")
                reg_check = 1
                if reg_check == 1:
                    with open(filename.strftime("found [%d-%m-%Y] [%H-%M-%S]")+".txt", "w") as found: 
                        found.write("")
                        found.write("IOC 1: found in het door u gekozen pad: " + basispad + '\\' + sleutel)
                winreg.CloseKey(key)
        except:
                reg_check = 2
                print("Registry entry " + sleutel + " not found.") 
                print("Registry IOC1 done")
                if reg_check == 2:
                    not_found_naam = 'not_found.txt'
                    not_found = open(not_found_naam, "w+")
                    not_found.write("IOC 1: not found in het door u gekozen pad: " + basispad + '\\' + sleutel)

        

                
    
def selectie_pad(scankeuze):
    if scankeuze == 'File':
        while True:
            
            uitgekozen_pad = input('U heeft gekozen voor de File Checker.\nBinnen welk pad wilt u zoeken?: ')
            bevestiging_pad = input('Is dit het juiste pad?: ' + uitgekozen_pad + '\nGelieve te bevestigen in de vorm "ja" of "nee": ')
            if bevestiging_pad == 'ja':
                break
            elif bevestiging_pad == 'nee':
                print('Voer opnieuw uw waarde in, aub')
            else:
                print('Dit is een verplicht veld, wilt u deze invullen aub')
        return uitgekozen_pad

def calc_hash(scankeuze, uitgekozen_pad):
    if scankeuze == 'File':
        lijst = []
        print('Het door u gekozen pad is: ' + uitgekozen_pad)
        for root, dirs,files in os.walk(uitgekozen_pad, topdown=True):
            for name in files:
                print(os.path.join(root, name))
                FileName = (os.path.join(root, name))
        

                hasher = hashlib.md5()
                with open(str(FileName), 'rb') as afile:
                    buf = afile.read()
                    hasher.update(buf)
                print(hasher.hexdigest())
                lijst.append(FileName)
                lijst.append(hasher.hexdigest())
                print(lijst)
                
""" Dit deel gaat de gemaakte hashlijst van de bestanden controleren met een bestaande hashlijst
def check_hash(hashes_bestanden):                           #hashes_bestanden is dan de gemaakte lijst met hashes van de bestanden
    with open(hashes_bestanden, 'r') as bestand1:
        with open('hashes.txt', 'r') as bestand2:           #hashes.txt is dan de file met hashes
            same = set(bestand1).intersection(bestand2)

    same.discard('\n')

    with open('gevonden_hashes.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)
"""
                
def main():
    scankeuze = kiezen_optie()
    basispad = Opstellen_pad(scankeuze)
    sleutel = Opstellen_sleutel(scankeuze)
    Register_IOC1(scankeuze, basispad, sleutel)
    uitgekozen_pad = selectie_pad(scankeuze)
    calc_hash(scankeuze, uitgekozen_pad)
#    check_hash(hashes_bestanden)

if __name__=='__main__':
    main()

    # de output moet vergeleken worden met hashwaardes uit een tekstbestand
    # aan het einde van de stappen moet de gebruiker terug kunnen gaan naar het begin
        # alle gekozen paden moeten altijd opgeslagen worden en aan het einde tegelijk gerund worden (.exe)
