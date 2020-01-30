import hashlib, os, sys

#Joyce
#De gebruiker krijgt hier 3 opties te zien waaruit gekozen kan worden.
#Bij elke cijferwaarde die gekozen kan worden hoort een waarde
#Elk van deze waardes heeft vervolgens zijn eigen functie.
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

#/Joyce
#Robin
def register_input(scankeuze):
    if scankeuze == 'Registry':                                                                                             #In deze functie worden de basiswaarde en de sleutel/map ingevoerd door de gebruiker en gesplitst. 
        try:                                                                                                                #Deze gesplitste basiswaarde wordt geebruikt om te bepalen of de gebbruiker een geldige waarde heeft ingevoerd.
            check = 0
            reg_invoer = input('U heeft gekozen voor de Registry Checker.\nGeef het pad op dat u wilt zoeken: ')
            hkey = reg_invoer.split('\\')[0]
            reg_path = reg_invoer.split('\\')[1]
            
            while True: 
                if hkey != 'HKEY_CLASSES_ROOT' and hkey != 'HKEY_CURRENT_USER' and hkey != 'HKEY_LOCAL_MACHINE' and hkey != 'HKEY_USERS' and hkey != 'HKEY_CURRENT_CONFIG':             #De controle wordt hier uitgevoerd, zodra het basispadd niet overeenkomt met de bekende paden, wordt er gevraagd een nieuwe waarde in te voeren.
                    reg_invoer = input('Dit is een ongeldige waarde, voer AUB een geldige waarde in: ')                                                                                 #Dit proces wordt herhaald tot er een geldige waarde wordt ingevoerd.
                    hkey = reg_invoer.split('\\')[0]
                    reg_path = reg_invoer.split('\\')[1]
                else:
                    break
#/Robin
#Alex
            # de gebruiker wordt hier gevraagd om het pad te bevestigen
            # invoer 'ja' schrijft het pad weg naar reg_invoer.txt
            # wanneer geen 'ja' wordt ingevoerd moet de gebruiker het pad opnieuw invoeren of terugkeren naar het hoofdmenu
            bevestiging = input('Is dit het juiste pad?: ' + reg_invoer + '\nGelieve te bevestigen in de vorm "ja" of "nee": ')
            while True:
                if bevestiging == 'ja':
                    with open('reg_invoer.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + reg_path + '\n')
                        file_out.close()
                        check = 'ja'
                        print(reg_invoer + ' wordt weggeschreven naar reg_invoer.txt.\n')
                    break
                elif bevestiging == 'nee':
                    check = input('Wilt u het nogmaals proberen? Antwoord met "ja" of "nee", aub: ')
                    if check == 'ja':
                        print('Voer opnieuw uw waarde in, aub')
                        register_input(scankeuze)
                    elif check == 'nee':
                        print('U gaat terug naar het hoofdmenu')
                    break
                else:
                    check = input('Wilt u het nogmaals proberen? Antwoord met "ja" of "nee", aub: ')
                    if check == 'ja':
                        print('Voer opnieuw uw waarde in, aub')
                        register_input(scankeuze)
                    elif check == 'nee':
                        print('U gaat terug naar het hoofdmenu')
                    break
            return check
        except:
            print("Er is een ongeldig pad ingevoerd.")
            register_input(scankeuze)
#/Alex

#Joyce
#Als aan het begin nummer 2 wordt gekozen wordt de variabele scankeuze daar op File gezet
#In deze functie kan de gebruiker een pad invoeren waarbinnen hij de bestanden wil scannen
#Dit pad wordt dan teruggegeven en er wordt om een bevestiging gevraagd
#Dit pad wordt dan weggeschreven naar een tekstbestand dat later in de tool gebruikt wordt.
def selectie_pad(scankeuze):
        if scankeuze == 'File':  
            try:
                check = 0
                uitgekozen_pad = input('U heeft gekozen voor de File Checker.\nBinnen welk pad wilt u zoeken?: ')
                while True:
                    bevestiging_pad = input('Is dit het juiste pad?: ' + uitgekozen_pad + '\nGelieve te bevestigen in de vorm "ja" of "nee": ')
                    if bevestiging_pad == 'ja':
                        with open('file_invoer.txt', 'a+') as file_out:
                            file_out.write(uitgekozen_pad + '\n')
                            file_out.close()
                            check = 'ja'
                            print(uitgekozen_pad + ' wordt weggeschreven naar file_invoer.txt.\n')
                        break
                    elif bevestiging_pad == 'nee':
                        check = input('Wilt u het nogmaals proberen? Antwoord met "ja" of "nee", aub: ')
                        if check == 'ja':
                            print('Voer opnieuw uw waarde in, aub')
                            selectie_pad(scankeuze)
                        elif check == 'nee':
                            print('U gaat terug naar het hoofdmenu')
                        break
                    else:
                        check = input('Wilt u het nogmaals proberen? Antwoord met "ja" of "nee", aub: ')
                        if check == 'ja':
                            print('Voer opnieuw uw waarde in, aub')
                            selectie_pad(scankeuze)
                        elif check == 'nee':
                            print('U gaat terug naar het hoofdmenu')
                        break
                return uitgekozen_pad
            except:
                print("Er is een ongeldig pad ingevoerd.")
                selectie_pad(scankeuze)
#/Joyce

#Robin
def main():                                                                                                                             #De main is op deze manier opgesteld zodat er meerdere waarder ingevoerd kunnen worden, waarna het programma automatisch teruggaat naar het hoofdmenu. 
    while True:                                                                                                                         #Er is een exit-beveiliging ingebouwd zodat de gebruiker op de hoogte is van het feit dat het scritpt afgesloten wordt. 
        scankeuze = kiezen_optie()  
        if scankeuze == 'Registry': 
            check = register_input(scankeuze)
        elif scankeuze == 'File':
            check = selectie_pad(scankeuze)
        elif scankeuze == 'Exit':
            check = input('Weet u zeker dat u het programma wilt verlaten?: Antwoorden met "ja" of "nee", aub: ')
            if check == 'ja':
                break
            elif check == 'nee':
                print('U gaat terug naar het hoofdmenu.' + '\n')
    exit
#/Robin



if __name__ == '__main__':
    main()
