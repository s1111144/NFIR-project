import winreg

invoer = 'HKEY_CLASSES_ROOT\Software'
hkey = invoer.split('\\', 1)[0]
path = invoer.split('\\', 1)[1]
print ('- Input: ' + invoer)
print ('- HKEY_*: ' + hkey)
print ('- Path: ' + path)

try:
    if hkey == 'HKEY_CLASSES_ROOT':
        reg1 = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path)
        print("found HKEY_CLASSES_ROOT\\" + path)
        winreg.CloseKey(reg1)
except:
    pass
finally:
    try:
        if hkey == 'HKEY_CURRENT_USER':
            reg2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
            print("found HKEY_CURRENT_USER\\" + path)
            winreg.CloseKey(reg2)
    except:
        pass
    finally:
        try:
            if hkey == 'HKEY_LOCAL_MACHINE':
                reg3 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
                print('found HKEY_LOCAL_MACHINE\\' + path)
                winreg.CloseKey(reg3)
        except:
            pass
        finally:
            try:
                if hkey == 'HKEY_USERS':
                    reg4 = winreg.OpenKey(winreg.HKEY_USERS, path)
                    print('found HKEY_USERS\\' + path)
                    winreg.CloseKey(reg4)
            except:
                pass
            finally:
                try:
                    if hkey == 'HKEY_CURRENT_CONFIG':
                        reg5 = winreg.OpenKey(winreg.HKEY_CURRENT_CONFIG, path)
                        print('found HKEY_CURRENT_CONFIG\\' + path)
                        winreg.CloseKey(reg5)
                except:
                    print('not found') # dit werkt niet? de gebruiker krijgt nu geen bericht als het pad niet bestaat
 
