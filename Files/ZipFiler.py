"""
Create Zip File Maker - The user enters various files from different directories
and the program zips them up into a zip file. Optional: Apply actual compression
to the files. Start with Huffman Algorithm.
"""
import zipfile
import os

f = input("Directory location to zip: ")
with zipfile.ZipFile('my_archive.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
  # my_zip.write('file1.txt')
  for folder, sub_folders, files in os.walk(f):
     print(f"Currently looking at {folder}")
     for f in files:
         print(f'\tFiles: {f}')
         my_zip.write(os.path.join(folder, f))
