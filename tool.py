import hashlib, os, sys
import winreg
from datetime import datetime
import time
import socket
now = datetime.now()
myhost = socket.gethostname()


#Robin
def registry():
    start = time.time()
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
#/Robin
#Alex
            try:
                        
                if hkey == 'HKEY_CLASSES_ROOT':
                    datum = now.strftime("%d/%m/%Y %H:%M:%S")
                    reg = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n - Found ' + datum + '\n\n')
                        file_out.close()
                    print('found')
                    print(datum)
                    winreg.CloseKey(reg)

                elif hkey == 'HKEY_CURRENT_USER':
                    datum = now.strftime("%d/%m/%Y %H:%M:%S")
                    reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n + Found ' + datum + '\n\n')
                        file_out.close()
                    print('found')
                    winreg.CloseKey(reg)
                
                elif hkey == 'HKEY_LOCAL_MACHINE':
                    datum = now.strftime("%d/%m/%Y %H:%M:%S")
                    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n + Found ' + datum + '\n\n')
                        file_out.close()
                    print('found')
                    winreg.CloseKey(reg)

                elif hkey == 'HKEY_USERS':
                    datum = now.strftime("%d/%m/%Y %H:%M:%S")
                    reg = winreg.OpenKey(winreg.HKEY_USERS, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n + Found ' + datum + '\n\n')
                        file_out.close()
                    print('found')
                    winreg.CloseKey(reg)

                elif hkey == 'HKEY_CURRENT_CONFIG':
                    datum = now.strftime("%d/%m/%Y %H:%M:%S")
                    reg = winreg.OpenKey(winreg.HKEY_CURRENT_CONFIG, path)
                    with open('reg_found.txt', 'a+') as file_out:
                        file_out.write(hkey + ' ' + path + '\n + Found ' + datum + '\n\n')
                        file_out.close()
                    print('found')
                    winreg.CloseKey(reg)
            except:
                with open('reg_found.txt', 'a+') as file_out:
                    datum = now.strftime("%d/%m/%Y %H:%M:%S")
                    file_out.write(hkey + ' ' + path + '\n - Not Found ' + datum + '\n\n')
                    file_out.close()
                print('not found')
#/Alex
#Joyce      
    except:
        pass

    end = time.time()
    duur = (end - start)
    duur = ("%.2f" % duur)

    with open("reg_found.txt", "a") as file_out:
        file_out.write("De duur van de scan is: " + str(duur))
        file_out.close()

    with open("reg_found.txt", "r") as file_out:
        if '+' in file_out.read():
            naam = 1
            file_out.close()        
        else:
            naam = 0
            file_out.close()

    if naam == 1:
        os.rename("reg_found.txt", "Found - Registry Log [" + myhost + "].txt")

    elif naam == 0:
        os.rename("reg_found.txt", "Not Found - Registry Log [" + myhost + "].txt")
#/Joyce
#Paulina
def file():
##    try:
        x=0
        lijst = []
        lijst2 = [line.rstrip('\n') for line in open('hashes.txt', 'r')]
        uitgekozen_paden = [line.rstrip('\n') for line in open('file_invoer.txt', 'r')]
        FileNames = []
        intersection = set(lijst).intersection(lijst2)
        difference = set(lijst) - set(lijst2)
        #print(intersection)

        for entry in uitgekozen_paden:
            uitgekozen_pad = entry
#/Paulina
#Alex
            for root, dirs, files in os.walk(uitgekozen_pad, topdown=True):
                for name in files:
                    FileNames.append(os.path.join(root, name))
                    print(FileNames)
                    with open(name, 'rb') as afile:
                        hasher = hashlib.md5()
                        buf = afile.read()
                        hasher.update(buf)
                    lijst.append(hasher.hexdigest())
                    print(hasher.hexdigest())
        ##                lijst.append(FileName)
#/Alex
#Pauline
                    
                    with open('gevonden_hashes.txt', 'w') as file_out:
                        for line in intersection:
                            file_out.write(FileName + "\t" + line + "\t" + "Found" + "\n")
                        for line in difference:
                            file_out.write(FileName + "\t" + line + "\t" + "Not found" + "\n")
                    print(FileName)

                    
                        lijst.append(hasher.hexdigest())
                        print(hasher.hexdigest())
                        with open('gevonden_hashes.txt', 'w') as file_out:
                            for names in FileNames:
                                naam = FileNames[x]
                                file_out.write(naam + "\t" + "Found" + "\n")
                                for line in difference:
                                    file_out.write(name + "\t" + line + "\t" + "Not found" + "\n")


##    except:
##        pass
#/Paulina




def main():
    registry()
    file()
    

if __name__=='__main__':
    main()
