from _winreg import *

#
# IOC 1
#
print("IOC 1")
try:
    reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    key = OpenKey(reg, 'SOFTWARE\LegitCorp\Version')
    value = QueryValue(key, None)

    if value == "0x19":
        print("Found IOC 0x19 in SOFTWARE\LegitCorp\Version registry key.")
    else:
        print("SOFTWARE\LegitCorp\Version registry key exists, but does not contain 0x19! Value is: %s" % value)

    CloseKey(key)
except:
    print("Registry key SOFTWARE\LegitCorp\Version not found!")
print("IOC 1 Done")

#
# IOC 2
#
print("\nIOC 2")
print("Checking for malicious value in SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
try:
    reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    key = OpenKey(reg, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run')

    counter = 0
    while True:
        try:
            value = EnumValue(key, counter)

            if "cscript.exe //nologo //e:jscript" in value[1]:
               print "Found compromised entry '%s' with content '%s'" % (value[0], value[1])

            counter += 1
        except(WindowsError):
            break


    CloseKey(key)
except:
    print("Registry key SOFTWARE\Microsoft\Windows\CurrentVersion\Run not found!")
print("IOC 2 Done")
