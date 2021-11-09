#!/usr/bin/env python3
# This is a python script to iterate through syllabi
# and convert file contents into string for natural language processing 

import glob
import csv
import os
import re
import argparse
import sys
import pdfplumber
import docx
import logging
import subprocess


logging.basicConfig(filename='err.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
log = logging.getLogger(__name__)

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        print("This is NOT a valid directory")
        sys.exit() 

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', required=True, type=dir_path, help='Location of your files')
parser.add_argument('-e', '--extension', required=True, type=str, help='Extension you are globbing for')
args = parser.parse_args()

def stringParser(path, ext):
    results = []
    output = []
    if ext == "pdf":
        files=str(path + "/*." + ext)
        files=glob.glob(files)
        for file in files:
            results.append(file.split("/")[-1])
            text=""
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text+=str(page.extract_text())
            results.append(text)
            output.append(results[:])
            results[:]=[]
        variables = ['File_name', 'Corpus']
        with open('pdfToString', 'w') as table:
            write = csv.writer(table)
            write.writerow(variables)
            write.writerows(output)
    elif ext == "docx":
        files=str(path + "/*." + ext)
        files=glob.glob(files)
        for file in files:
            results.append(file.split("/")[-1])
            try:
                doc = docx.Document(file)
                allText = []
                for para in doc.paragraphs:
                    text = para.text.encode('ascii', 'ignore')
                    allText.append(text)
                stringlist=[x.decode('utf-8') for x in allText]
                string = ''.join(stringlist)
                results.append(string)
                output.append(results[:])
                results[:]=[]
            except Exception:
                print("file not a valid .docx file")
                log.error("File " + file + " is not a valid .docx file, please check this file")
        variables = ['File_name', 'Corpus']
        with open('docxToString', 'w') as table:
            write = csv.writer(table)
            write.writerow(variables)
            write.writerows(output)
    else: 
        print("Format not supported by this function")
# Run function 
stringParser(args.directory, args.extension)
