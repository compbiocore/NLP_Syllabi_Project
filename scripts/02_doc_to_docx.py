# Converts .doc files to .docx files

# Note: Need to install libreoffice via homebrew first 

import os, os.path
import glob
import subprocess

# Change the path variable as needed 
path = "/Users/jordan/Desktop/NLP_Syllabi_Project/syllabi"
print(len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]))

files=str(path + "/*." + "doc")
files=glob.glob(files)
os.chdir(path)
for file in files:
    subprocess.call(['soffice', '--headless', '--convert-to', 'docx', file])

print(len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]))
