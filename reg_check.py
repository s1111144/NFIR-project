import winreg

check = 0
invoer = input('Geef het pad op dat u wilt zoeken: ')
bevestiging = input('Is dit het juiste pad?: ' + invoer + '\nGelieve te bevestigen in de vorm "ja" of "nee": ')
while True:
    if bevestiging == 'ja':
        break
    elif bevestiging == 'nee':
        print('Voer opnieuw uw waarde in, aub') #na deze begint hij niet opnieuw
        break
    else:
        print('Dit is een verplicht veld, wilt u deze invullen aub') #na deze begint hij niet opnieuw
        break







hkey = invoer.split('\\')[0]
path = invoer.split('\\')[1]
##print ('- Input: ' + invoer)
##print ('- HKEY_*: ' + hkey)
##print ('- Path: ' + path)

try:
    if hkey == 'HKEY_CLASSES_ROOT':
        reg = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path)
        print('found: ' + invoer)
        winreg.CloseKey(reg)

    elif hkey == 'HKEY_CURRENT_USER':
        reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
        print('found: ' + invoer)
        winreg.CloseKey(reg)

    elif hkey == 'HKEY_LOCAL_MACHINE':
        reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        print('found: ' + invoer)
        winreg.CloseKey(reg)

    elif hkey == 'HKEY_USERS':
        reg = winreg.OpenKey(winreg.HKEY_USERS, path)
        print('found: ' + invoer)
        winreg.CloseKey(reg)

    elif hkey == 'HKEY_CURRENT_CONFIG':
        reg = winreg.OpenKey(winreg.HKEY_CURRENT_CONFIG, path)
        print('found: ' + invoer)
        winreg.CloseKey(reg)
except:
    pass
    check = 2
    if check == 2:
        print('not found: ' + invoer)
        # 'not found' wordt niet weergeven als:
            # de eerste letter van Path geen hoofdletter is
            # de HKEY niet bestaat
