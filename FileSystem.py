import os                                       # For File System
from pathlib import Path                        # For File System
from datetime import date                       # For Datetime
from time import ctime                          # For Time Conversion
import shutil                                   # For File Copy
from zipfile import ZipFile

source_path = r'C:/Users/subha/Downloads'
path = Path(source_path)


# CHECKS HOW MANY ARE FILES AND FOLDERS IN PATH
fno = 0
dno = 0
for name in path.iterdir():
    if os.path.isfile(name):
        fno += 1
    else:
        dno += 1
print("Total Files:", fno, "  Total Folders:", dno)

print("*" * 150)

# GET FILE INFORMATION (NAME, DATE CREATED, SIZE)
for file_name in path.glob("S*.pdf"):
    print("FILE NAME:", file_name, " DATE CREATED:", ctime(file_name.stat().st_ctime), " FILE SIZE:", file_name.stat().st_size)
    # This will overwrite the existing file.
    # file_name.write_text("This is MS Office Serial No.")

    # This will read the existing file contents.
    # print(file_name.read_text())

print("*" * 150)

# CONVERT DATE INTO YYYYMMDD
today = str(date.today())
today = str(today.replace("-", ""))


# CREATES NEW FOLDER
target_folder = Path(source_path+"/"+today)
if not Path(target_folder).exists():
    target_folder.mkdir(parents=True, exist_ok=True)
    print(target_folder, " Folder is created")
else:
    print('Folder is already exists!')

print("*" * 150)

# ZIP FILE AND COPY TO TARGET FOLDER
zip_file = ZipFile(str(target_folder) + "/" + today, "w")
# CREATE ZIP FILE WITH SOURCE FOLDER FILE TO TARGET FOLDER
for file_name in path.glob("S*.Zip"):
    zip_file.write(file_name)

    # MOVE FILE TO DESTINATION FOLDER
    # shutil.move(file_name, str(target_folder))
zip_file.close()
