# 
print("Filler IOC1") 
try: 
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) 
    key = winreg.OpenKey(reg, 'SOFTWARE\LegitCorp') 
 
    print("IOC1: LegitCorp found.") 
 
    winreg.CloseKey(key) 
except: 
    print("Registry key SOFTWARE\LegitCorp not found!") 
print("Filler IOC 1 Done") 
 
# 
# IOC 2 
# 
print("\nFiller IOC 2") 
print("Checking for malicious value in SOFTWARE\Microsoft\Windows\CurrentVersion\Run") 
try: 
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) 
    key = winreg.OpenKey(reg, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run') 
 
    counter = 0 
    while True: 
        try: 
            value = winreg.EnumValue(key, counter) 
 
            if "cscript.exe //nologo //e:jscript" in value[1]: 
               print ("Found compromised entry '%s' with content '%s'" % (value[0], value[1])) 
 
            counter += 1 
        except(WindowsError): 
            break 
 
 
    winreg.CloseKey(key) 
except: 
    print("Registry key SOFTWARE\Microsoft\Windows\CurrentVersion\Run not found!") 
print("FIller IOC 2 Done")


print("\nBaldr IOC1") 
try: 
    reg = winreg.ConnectRegistry(None, winreg.HKCU) 
    key = winreg.OpenKey(reg, 'SOFTWARE\Microsoft\key') 
 
    print("Baldr IOC1: SOFTWARE\Microsoft\key found.") 
 
    winreg.CloseKey(key) 
except: 
    print("Registry key SOFTWARE\Microsoft\key not found!") 
print("Baldr IOC 1 Done") 
