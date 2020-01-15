import os
import stat
import datetime as dt
import argparse
from pprint import pprint

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


def selectie_hoeveelheid():
    while True:
            
        uitgekozen_hoeveelheid = input('Hoeveel bestanden wilt u doorzoeken?: ')
        bevestiging_hoeveelheid = input('Is dit de juiste hoeveelheid?: ' + uitgekozen_hoeveelheid + '\nGelieve te bevestigen in de vorm "ja" of "nee": ')
        if bevestiging_hoeveelheid == 'ja':
            break
        elif bevestiging_hoeveelheid == 'nee':
            print('Voer opnieuw uw waarde in, aub')
        else:
            print('Dit is een verplicht veld, wilt u deze invullen aub')
    return uitgekozen_hoeveelheid

def print_files(num_files, directory):
    """
    gets a list of files sorted by modified time

    keyword args:
    num_files -- the n number of files you want to print
    directory -- the starting root directory of the search

    """
    modified = []
    accessed = []
    rootdir = os.path.join(os.getcwd(), directory)

    for root, sub_folders, files in os.walk(rootdir):
        for file in files:
            try:
                unix_modified_time = os.stat(os.path.join(root, file))[stat.ST_MTIME]
                unix_accessed_time = os.stat(os.path.join(root, file))[stat.ST_ATIME]
                human_modified_time = dt.datetime.fromtimestamp(unix_modified_time).strftime('%Y-%m-%d %H:%M:%S')
                human_accessed_time = dt.datetime.fromtimestamp(unix_accessed_time).strftime('%Y-%m-%d %H:%M:%S')
                filename = os.path.join(root, file)
                modified.append((human_modified_time, filename))
                accessed.append((human_accessed_time, filename))
            except:
                pass

    modified.sort(key=lambda a: a[0], reverse=True)
    accessed.sort(key=lambda a: a[0], reverse=True)
    print('Modified')
    pprint(modified[:num_files])
    print('Accessed')
    pprint(accessed[:num_files])


def main():
    uitgekozen_pad = selectie_pad()
    uitgekozen_hoeveelheid = selectie_hoeveelheid()
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
                        '--number',
                        help='number of items to return',
                        type=int,
                        default=uitgekozen_hoeveelheid)
    parser.add_argument('-d',
                        '--directory',
                        help='specify a directory to search in',
                        default=uitgekozen_pad)

    args = parser.parse_args()

    print_files(args.number, args.directory)


if __name__=='__main__':
    main()
