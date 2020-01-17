import winreg

invoer = 'HKEY_CLASSES_ROOT\.3g2\OpenWithProgids'
hkey = invoer.split('\\', 1)[0]
path = invoer.split('\\', 1)[1]
print ('- Input: ' + invoer)
print ('- HKEY_*: ' + hkey)
print ('- Path: ' + path)

try:
    reg1 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path)
    print("found HKEY_CLASSES_ROOT\\" + path)
    winreg.CloseKey(reg1)
except:
    try:
        reg2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
        print("found HKEY_CURRENT_USER\\" + path)
        winreg.CloseKey(reg2)
    except:
        try:
            reg3 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            print('found HKEY_LOCAL_MACHINE\\' + path)
            winreg.CloseKey(reg3)
        except:
            try:
                reg4 = winreg.OpenKey(winreg.HKEY_USERS, path)
                print('found HKEY_USERS\\' + path)
                winreg.CloseKey(reg4)
            except:
                try:
                    reg5 = winreg.OpenKey(winreg.HKEY_CURRENT_CONFIG, path)
                    print('found HKEY_CURRENT_CONFIG\\' + path)
                    winreg.CloseKey(reg5)
                except:
                    print('not found')
                        
