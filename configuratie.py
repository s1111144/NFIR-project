import hashlib, os, sys

#Joyce
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
    if scankeuze == 'Registry':
        try:
            check = 0
            reg_invoer = input('U heeft gekozen voor de Registry Checker.\nGeef het pad op dat u wilt zoeken: ')
            hkey = reg_invoer.split('\\')[0]
            reg_path = reg_invoer.split('\\')[1]
            
            while True: 
                if hkey != 'HKEY_CLASSES_ROOT' and hkey != 'HKEY_CURRENT_USER' and hkey != 'HKEY_LOCAL_MACHINE' and hkey != 'HKEY_USERS' and hkey != 'HKEY_CURRENT_CONFIG':
                    reg_invoer = input('Dit is een ongeldige waarde, voer AUB een geldige waarde in: ')
                    hkey = reg_invoer.split('\\')[0]
                    reg_path = reg_invoer.split('\\')[1]
                    break
#/Robin
#Alex                
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
                        print('Voer opnieuw uw waarde in, aub') #na deze begint hij niet opnieuw
                        register_input(scankeuze)
                    elif check == 'nee':
                        print('U gaat terug naar het hoofdmenu')
                    break
                else:
                    check = input('Wilt u het nogmaals proberen? Antwoord met "ja" of "nee", aub: ')
                    if check == 'ja':
                        print('Voer opnieuw uw waarde in, aub') #na deze begint hij niet opnieuw
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
def selectie_pad(scankeuze):
        while True:
            uitgekozen_pad = input('U heeft gekozen voor de File Checker.\nBinnen welk pad wilt u zoeken?: ')
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
                    print('Voer opnieuw uw waarde in, aub') #na deze begint hij niet opnieuw
                    selectie_pad(scankeuze)
                elif check == 'nee':
                    print('U gaat terug naar het hoofdmenu')
            else:
                print('Dit is een verplicht veld, wilt u deze invullen aub')
        return uitgekozen_pad
#/Joyce

#Robin
def main():
    while True:
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