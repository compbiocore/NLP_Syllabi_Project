# This is a for converting parsed syllabi files to .csv files 

import os, os.path
import glob
import pandas as pd
import docx
from functools import reduce
import numpy as np

df_docx = pd.read_csv("/Users/jordan/Desktop/NLP_Syllabi_Project_Git/data_and_output/docxToString", error_bad_lines=False)
df_pdf = pd.read_csv("/Users/jordan/Desktop/NLP_Syllabi_Project_Git/data_and_output/pdfToString", error_bad_lines=False)
print(df_docx.dtypes)
print(df_pdf.dtypes)
df_docx['Corpus'] = df_docx['Corpus'].astype('string')
df_pdf['Corpus'] = df_pdf['Corpus'].astype('string')
print(df_docx.dtypes)
print(df_pdf.dtypes)
df_docx.to_csv("docxToSTring.csv", index=True)
df_pdf.to_csv("pdfToSTring.csv", index=True)
