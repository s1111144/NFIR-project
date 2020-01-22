import hashlib, os, sys
import winreg
import datetime
filename = datetime.datetime.now()


def registry():
    try:
        with open('reg_invoer.txt', 'r') as inlezen:
            sleutels = inlezen.readlines()
            hkey_lijst = [k.split()[0] for k in sleutels]
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

            try:
                        
                if hkey == 'HKEY_CLASSES_ROOT':
                    reg = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n - Found ' + '[%d-%m-%Y] [%H-%M-%S]'+ '\n\n')
                        file_out.close()
                    print('found')
                    winreg.CloseKey(reg)

                elif hkey == 'HKEY_CURRENT_USER':
                    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n' + '- Found' + '\n\n')
                        file_out.close()
                    print('found')
                    winreg.CloseKey(reg)
                
                elif hkey == 'HKEY_LOCAL_MACHINE':
                    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n' + '- Found' + '\n\n')
                        file_out.close()
                    print('found')
                    winreg.CloseKey(reg)

                elif hkey == 'HKEY_USERS':
                    reg = winreg.OpenKey(winreg.HKEY_USERS, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n' + '- Found' + '\n\n')
                        file_out.close()
                    print('found')
                    winreg.CloseKey(reg)

                elif hkey == 'HKEY_CURRENT_CONFIG':
                    reg = winreg.OpenKey(winreg.HKEY_CURRENT_CONFIG, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n' + '- Found' + '\n\n')
                        file_out.close()
                    print('found')
                    winreg.CloseKey(reg)
            except:
                with open('reg_found.txt', 'a+') as file_out:
                    file_out.write(hkey + ' ' + path + '\n' + '- Not Found' + '\n\n')
                    file_out.close()
                print('not found')
    except:
        pass

def main():
    registry()
##    uitgekozen_pad = selectie_pad(scankeuze)
##    calc_hash(scankeuze, uitgekozen_pad)

if __name__=='__main__':
    main()
