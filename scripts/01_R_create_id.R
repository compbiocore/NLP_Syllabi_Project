# Split Syllabi .csv and create new syllabi csv with identifier variable

# Call in file 
library(readr)
setwd("/Users/jordan/Desktop/Git_folder/NLP_Syllabi_Project/data_and_output")
getwd()
syllabi_data <- read_csv("syllabi_data.csv")

names(syllabi_data)
syllabi_data$File_name<-gsub("^.*/", "", syllabi_data$path)
table(syllabi_data$File_name)
sum(is.na(syllabi_data$File_name))
sum(syllabi_data$File_name=="")
syllabi_data$File_name<-ifelse(syllabi_data$File_name=="", NA, 
                               ifelse(syllabi_data$original_name=="NULL", NA, syllabi_data$File_name)) 
# Need to do this because we will be working with .doc files that have been converted to .docx files and so 
# will need to merge based on this 
syllabi_data$File_name<-ifelse(substr(syllabi_data$File_name, 
                                      nchar(syllabi_data$File_name)-2, nchar(syllabi_data$File_name))=="doc", 
                               paste0(syllabi_data$File_name,"x"), syllabi_data$File_name)
sum(is.na(syllabi_data$File_name))
getwd()
write.csv(syllabi_data, "syllabi_data_2.csv")
