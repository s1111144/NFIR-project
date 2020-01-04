import os
import stat
import datetime as dt
import argparse
from pprint import pprint


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
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',
                        '--number',
                        help='number of items to return',
                        type=int,
                        default=999)
    parser.add_argument('-d',
                        '--directory',
                        help='specify a directory to search in',
                        default='C:/Users/Alex/Desktop')

    args = parser.parse_args()

    print_files(args.number, args.directory)

if __name__ == '__main__':
    main()





#######

#python -m pip install PyPiWin32

#code for reading windows events
log_handle = win32evtlog.OpenEventLog(server, log_type)

while there_are_events:
    events = win32evtlog.ReadEventLog(log_handle, flags, 0)

win32evtlog.CloseEventLog(log_handle)



begin_sec = time.time()
    begin_time = time.strftime('%H:%M:%S  ', time.localtime(begin_sec))
 
    seconds_per_hour = 60 * 60
    how_many_seconds_back_to_search = seconds_per_hour * number_of_hours_to_look_back
 
    gathered_events = []
 
    try:
        log_handle = win32evtlog.OpenEventLog(server, log_type)
 
        total = win32evtlog.GetNumberOfEventLogRecords(log_handle)
        print("Scanning through {} events on {} in {}".format(total, server, log_type))
 
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
 
        event_count = 0
        events = 1
        while events:
            events = win32evtlog.ReadEventLog(log_handle, flags, 0)
            seconds = begin_sec
            for event in events:
                the_time = event.TimeGenerated.Format()
                seconds = date2sec(the_time)
                if seconds < begin_sec - how_many_seconds_back_to_search: break
 
                if event.EventType == win32con.EVENTLOG_ERROR_TYPE:
                    event_count += 1
                    gathered_events.append(event)
            if seconds < begin_sec - how_many_seconds_back_to_search: break  # get out of while loop as well
 
        win32evtlog.CloseEventLog(log_handle)
    except:
        try:
            print(traceback.print_exc(sys.exc_info()))
        except:
            print('Exception while printing traceback')
 
    return gathered_events


#dan specifieke logs benoemen en als die gevonden worden moeten ze teruggegeven worden.
