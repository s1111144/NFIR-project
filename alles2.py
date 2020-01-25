import hashlib, os, sys
import winreg
import datetime
filename = datetime.datetime.now()

keuzes = []

def kiezen_optie():
    print('U heeft de mogelijkheid te kiezen uit:\n 1. Registry Checker\n 2. File Checker\n 3. Exit')
    while True:
        scankeuze = input('Welke van de opties wilt u kiezen? Voer de cijferwaarde in: ')
        if scankeuze == '1':
            scankeuze = 'Registry'
            break
        elif scankeuze == '2':
            scankeuze = 'File'
            break
        elif scankeuze == '3':
            scankeuze = 'Exit'
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

def Opstellen_sleutel(scankeuze, basispad):
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
        keuzes.append(basispad)
        keuzes.append(sleutel)
        print(keuzes)
        return sleutel

def Exit(scankeuze):
    if scankeuze == 'Exit':
        while True:
            bevestiging_keuze = input('Zijn deze paden correct? Gelieve te bevestigen in de vorm "ja" of "nee": ')
            if bevestiging_keuze == 'ja':
                print('EXE wordt aangemaakt')
                break
            elif bevestiging_keuze == 'nee':
                print('Dat is naar, begin maar opnieuw')
                exit()
            else:
                print('Dit is een verplicht veld, wilt u deze invullen aub')
                


# vanaf hier moet de .exe aangemaakt worden
# pas wanneer de .exe wordt uitgevoerd moet onderstaande code uitgevoerd worden

def Registry(keuzes):
    basispad = ''
    sleutel = ''
    if keuzes != '':
        for entry in keuzes:
            if keuze[x/2 == True]:
                basispad = entry
            else:
                sleutel = entry
        
    
      
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
        lijst2 = [line.rstrip('\n') for line in open("hashes.txt", 'r')]
        lijst3 = []

    
        print('Het door u gekozen pad is: ' + uitgekozen_pad)

        for root, dirs, files in os.walk(uitgekozen_pad, topdown=True):          
            for name in files:
                FileName = (os.path.join(root, name))
                hasher = hashlib.md5()
  
                with open(FileName, 'rb') as afile:
                    buf = afile.read()
                    hasher.update(buf)
                    lijst.append(FileName)
                    lijst.append(hasher.hexdigest())
                    hashes = (FileName + '\t' + hasher.hexdigest())
                    lijst3.append(hashes)
##                    print(lijst3)

            with open('namen_hashes.txt', 'w') as file_in:
                for line in lijst3:
                    file_in.write(line + '\t' + '\n')

            with open('test_hashes.txt', 'w') as hash_naam:
                for line in lijst:
                    hash_naam.write(line)

            with open('namen_hashes.txt', 'r') as inlezen: 
                invoer = inlezen.readlines()
                Naam = [N.split('\t')[0] for N in invoer]
                Hash = [H.split('\t')[1] for H in invoer]

            a = set(Hash)
            b = set(lijst2)
            intersection = a.intersection(b)
            difference = a - b
            print(intersection)
##            print(Hash)
##            print(lijst)

            with open('gevonden_hashes.txt', 'w') as file_out, open('test_hashes.txt', 'r') as volledig:
                test = volledig.readlines()
                print(test)
                if intersection in test:
                    print("it's here")
                    for line in intersection:
                        file_out.write("\t" + line + "\t" + "found" + "\n")
                else:
                    print("it's not here")
##                    for line in intersection:
##                        file_out.write("\t" + line + "\t" + "found" + "\n")
##                        print(line)

                             
##                with open('gevonden_hashes.txt', 'w+') as file_out, open('namen_hashes.txt', 'r') as file_in:
##                    invoer = file_in.readlines()
##                    Naam = [N.split('\t')[0] for N in invoer]
##                    Hash = [H.split('\t')[1] for H in invoer]
##                    if str(intersection) in invoer[1]:
##                        for line in intersection:
##                            print(intersection)
##                            file_out.write(Naam + intersection + "found" + "\n")
##                        for line in difference:
##                            file_out.write(naam + line + "not found" + "\n")
                                                


def main():
    scankeuze = kiezen_optie()
    basispad = Opstellen_pad(scankeuze)
    sleutel = Opstellen_sleutel(scankeuze, basispad)
    Exit(scankeuze)
    Register_IOC1(scankeuze, basispad, sleutel)
    uitgekozen_pad = selectie_pad(scankeuze)
    calc_hash(scankeuze, uitgekozen_pad)

if __name__=='__main__':
    main()

    # de output moet vergeleken worden met hashwaardes uit een tekstbestand
    # aan het einde van de stappen moet de gebruiker terug kunnen gaan naar het begin
        # alle gekozen paden moeten altijd opgeslagen worden en aan het einde tegelijk gerund worden (.exe)
