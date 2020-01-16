import hashlib, os, sys
import winreg

def kiezen_optie():
    print('U heeft de mogelijkheid te kiezen uit:\n 1. Registry Checker\n 2. File Checker')
    keuze = input('Welke van de opties wilt u kiezen? Voer de cijferwaarde in: ')

    


def Opstellen_pad():
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

def Opstellen_sleutel():
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
      

#
def Register_IOC1(basispad, sleutel): 
    try:
        if basispad == 'HKEY_CLASSES_ROOT':
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CLASSES_ROOT)
            key = winreg.OpenKey(reg, sleutel)
            print(sleutel + " found.")
            winreg.CloseKey(key)
        elif basispad == 'HKEY_CURRENT_USER':
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(reg, sleutel)
            print(sleutel + " found.")
            winreg.CloseKey(key)
        elif basispad == 'HKEY_LOCAL_MACHINE':
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            key = winreg.OpenKey(reg, sleutel)
            print(sleutel + " found.")
            winreg.CloseKey(key)
        elif basispad == 'HKEY_USERS':
            reg = winreg.ConnectRegistry(None, winreg.HKEY_USERS)
            key = winreg.OpenKey(reg, sleutel)
            print(sleutel + " found.")
            winreg.CloseKey(key)
        elif basispad == 'HKEY_CURRENT_CONFIG':
            reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_CONFIG)
            key = winreg.OpenKey(reg, sleutel)
            print(sleutel + " found.")
            winreg.CloseKey(key)
    except:
            print("Registry entry " + sleutel + " not found.") 
            print("Registry IOC1 done")

lijst = []

def selectie_pad():
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

def calc_hash(uitgekozen_pad):
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
            

            

def main():
    keuze = kiezen_optie()
    basispad = Opstellen_pad()
    sleutel = Opstellen_sleutel()
    print('Het door u gekozen pad is: ' + basispad + '\\' + sleutel)
    Register_IOC1(basispad, sleutel)
    uitgekozen_pad = selectie_pad()
    print('Het door u gekozen pad is: ' + uitgekozen_pad)
    calc_hash(uitgekozen_pad)
    print(lijst)

if __name__=='__main__':
    main()

    # de output moet nog verwerkt worden, zodat deze vergeleken kan worden met hashwaardes uit een tekstbestand
