import hashlib, os, sys
import winreg
import datetime
filename = datetime.datetime.now()


def registry():
    #try:
    with open('reg_invoer.txt', 'r') as inlezen:
        sleutels = inlezen.readlines()
##        print(sleutels[0])
        hkey_lijst = [k.split()[0] for k in sleutels]
        path_lijst = [p.split()[1] for p in sleutels]
##    print(hkey_lijst[1])
##    print(path_lijst[0])

    x = 0
    y = 0
    z = 3
    counter = 0

    while counter < z:
        x += 1
        y += 1
        hkey = hkey_lijst[x]
        print(hkey)
        path = path_lijst[y]
        print(path)
                    
        if hkey == 'HKEY_CLASSES_ROOT':
            reg = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path)
            print('found')
            winreg.CloseKey(reg)

        elif hkey == 'HKEY_CURRENT_USER':
            reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
            print('found')
            winreg.CloseKey(reg)
        
        elif hkey == 'HKEY_LOCAL_MACHINE':
            reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            print('found')
            winreg.CloseKey(reg)

        elif hkey == 'HKEY_USERS':
            reg = winreg.OpenKey(winreg.HKEY_USERS, path)
            print('found')
            winreg.CloseKey(reg)

        elif hkey == 'HKEY_CURRENT_CONFIG':
            reg = winreg.OpenKey(winreg.HKEY_CURRENT_CONFIG, path)
            print('found')
            winreg.CloseKey(reg)
##    except:
##        pass
##        check = 2
##        if check == 2:
##            print('not found')
##            # 'not found' wordt niet weergeven als:
##                # de eerste letter van Path geen hoofdletter is
##                # de HKEY niet bestaat





def main():
    registry()
##    uitgekozen_pad = selectie_pad(scankeuze)
##    calc_hash(scankeuze, uitgekozen_pad)

if __name__=='__main__':
    main()
