import os
from pathlib import Path
from datetime import date
from time import ctime



#Makd Date yyyymmdd
today = str(date.today())
today = today.replace("-", "")

Folder = r'C:\Users\subha\Downloads'
path = Path(Folder)
for name in path.iterdir():
    if os.path.isfile(name):
        print('File Name: ', name.name, " Date Created:", ctime(name.stat().st_ctime), " File Size:", name.stat().st_size)
    else:
        print('Folder : ', name.name)

for pdf in path.glob("*.pdf"):
    print(pdf)

new_folder = Path(Folder+"\\"+today)
if new_folder.exists():
    print('Folder is already exists!')
else:
    path.mkdir(today)
    print(Folder, " Folder is created")


