#!/usr/bin/python3
import sys
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) != 2:
    print('ERROR')
elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("Usage : backupfinder <URL>")
    exit()
else:
    file_name = sys.argv[1]

f = open("backup_extensions.txt", "r")
backup_types_list = f.read().split('\n')

for backup_type in backup_types_list:
    try:
        r = requests.get(file_name + backup_type)
        print(f"{bcolors.OKGREEN if r.status_code == 200 else '' }Got status code {r.status_code} for url {r.url}{bcolors.ENDC}")
    except: 
        print(f"{bcolors.FAIL}ERROR ON URL{bcolors.ENDC}")
        exit()