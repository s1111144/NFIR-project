import hashlib, os, sys

def selectie_pad():
    while True:
        
        uitgekozen_pad = input('Binnen welk pad wilt u zoeken?: ')
        bevestiging_pad = input('Is dit het juiste pad?: ' + uitgekozen_pad + '\nGelieve te bevestigen in de vorm "ja" of "nee": ')
        if bevestiging_pad == 'ja':
            break
        elif bevestiging_pad == 'nee':
            print('Voer opnieuw uw waarde in, aub')
        else:
            print('Dit is een verplicht veld, wilt u deze invullen aub')
    return uitgekozen_pad

def calc_hash(uitgekozen_pad):
    for root, dirs,files in os.walk(uitgekozen_pad, topdown=True):
        for name in files:
            print(os.path.join(root, name))
            FileName = (os.path.join(root, name))

            hasher = hashlib.md5()
            with open(str(FileName), 'rb') as afile:
                buf = afile.read()
                hasher.update(buf)
            print(hasher.hexdigest())

def main():
    uitgekozen_pad = selectie_pad()
    print('Het door u gekozen pad is: ' + uitgekozen_pad)
    calc_hash(uitgekozen_pad)

if __name__=='__main__':
    main()

    # de output moet nog verwerkt worden, zodat deze vergeleken kan worden met hashwaardes uit een tekstbestand
