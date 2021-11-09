# Merge syllabus files with base data 

setwd("/Users/jordan/Desktop/NLP_Syllabi_Project_Git/merge_files")
library(readr)
docx <- read_csv("docxToSTring.csv")
docx=docx[,-1]
pdf<- read_csv("pdfToSTring.csv")
pdf=pdf[,-1]
data <- read_csv("syllabi_data_2.csv")

library(dplyr)
merge<-left_join(data, pdf, by="File_name")
merge<-left_join(merge, docx, by="File_name")
merge<-merge %>% mutate(Corpus = coalesce(Corpus.x,Corpus.y)) 
names(merge)
merge<-merge[,-c(13,14)]
merge<-merge[!duplicated(merge),]
getwd()
setwd("/Users/jordan/Desktop")
write.csv(merge, "merged_data_clean.csv")
