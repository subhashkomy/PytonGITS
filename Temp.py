import os
import zipfile


def create_zip(source_folder, target_folder, zip_file_name, file_type):
    # target_folder = 'C:\\Users\\subha\\Downloads\\20230120\\'
    # zip_file_name = 'MyPDFsZipFile.zip'
    # file_type = '.pdf'
    zip_source = target_folder + zip_file_name
    process_file = zipfile.ZipFile(zip_source, 'w')

    # source_folder = 'C:\\Users\\subha\\Downloads'
    os.chdir(source_folder)

    for x in os.listdir():
        if x.endswith(file_type):
            process_file.write(x, compress_type=zipfile.ZIP_DEFLATED)
    process_file.close()


# create_zip(target_folder='C:\\Users\\subha\\Downloads\\20230120\\', source_folder='C:\\Users\\subha\\Downloads',
#            zip_file_name='MyPDFsZipFile.zip', file_type = '.pdf')
