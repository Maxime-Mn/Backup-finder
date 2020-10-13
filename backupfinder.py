#!/usr/bin/python3
import sys
import requests
from bcolors import Bcolors 

if len(sys.argv) != 2:
    print('ERROR')
elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
    print("Usage : backupfinder <URL>")
    exit()
else:
    file_name = sys.argv[1]

f = open("backup_extensions.txt", "r")
backup_types_list = f.read().split('\n')
bcolors = Bcolors

for backup_type in backup_types_list:
    try:
        r = requests.get(file_name + backup_type)
        print(f"{bcolors.OKGREEN if r.status_code == 200 else '' }Got status code {r.status_code} for url {r.url}{bcolors.ENDC}")
    except: 
        print(f"{bcolors.FAIL}ERROR ON URL{bcolors.ENDC}")
        exit()
