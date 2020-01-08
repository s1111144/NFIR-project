import winreg

REG_PATH = "id"


def CheckRegKey():
    var = 'var'
    hit = 'hit'
    returner = 'return'
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, 'name')
        winreg.CloseKey(registry_key)
        if value == '5':
            return hit
        else:
            print('not found')
            return returner
    except WindowsError:
        return var
    








if __name__ == '__main__':
    var = CheckRegKey()
    print(var)

