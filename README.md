# NLP_Syllabi_Project

This repo tracks the process of developing an interactive natural language processing (NLP) web application for Brown's Library Planning and Assessment team. The goal of this project was to analyze Brown University course syllabi via NLP to identify how race and racial issues appear in courses at Brown. The Brown course syllabi are in a shared folder on google drive and you will need to request permission to the shared folder to start this analysis pipeline from the very beginning. The folder contains roughly 5,000 course syllabi from various departments across Brown University. 

# Organization overview 

 - The `scripts` folder contains all the scripts needed for parsing and cleaning the raw syllabi and setting up the data set needed to begin preprocessing. These scripts are sequentially numbered and are to be run in numerical order. 
 
 - The `metadata` folder contains two folders: 1.) a folder for containerizing the NLP web app (`docker`); and 2.) a folder containing the data files used in the steps to create a final merged, cleaned data set that contains syllabi content as corpus (`data`). Note that the `docker` folder contains other files, such as a .py notebook and data file as well; these files are all needed for the docker image to be successfully built and deployed as a web app (discussed in steps below). 
 
 - The `notebooks` folder contains the jupyter notebooks used to preprocess the data and create an interactive dashboard (with widgets) allowing for interactive exploratory and nlp analysis. The `web.py` notebook in this folder is also in the `docker` folder, as it is needed there for deployment of the web app. 
 
 # Process  
 
 ## Part 1: Scripts 
 
 1. We first ran the R script titled `01_R_create_id.R` to create a suitable id variable within the data that would later allow us to merge the course data we already had from the planning and assessment team with the corpus data that we create when we parse through the course syllabi and extract the syllabi content as strings. 
 
 2. Next, we ran the `02_doc_to_docx.py` script to iterate through our folder of syllabi and identify and convert all .doc files to .docx files. 
 
 3. Next we created a parser function that we can use from the command line with the `03_parser.py` script. This parser allows the user to specify a directory and a file extension type from the command line to then check if the user has specified a valid directory and, if so, parse through a folders contents and extract out the contents of each file within the folder as a python string. The command is used as follows: `stringParser -d <directory> -e <file extension>` 
 
 4. After parsing through the course syllabi and extracting out syllabi content, we ran the `04_convert_to_csv.py` script to convert this parsed information to .csv files. 
 
 5. Lastly, we ran the `05_R_merge.R` script to merge the .csv files containing course syllabi content as strings with the data we already had from Brown courses. This steps creates a final data set called `merged_data_clean.csv` that is then used to start the preprocessing step, which gets the data ready for NLP. 
 
 ## Part 2: Notebooks 
 
 After step 5 from the previous section, you can use the Jupyter notebooks to preprocess and analyze your data interactively. 
 
### Pre-processing 

Launch JupyterLab and use the `Pre_processing.ipynb` notebook to pre-process the course syllabi data and get it ready for natural language processing. This notebook performs things such as removing low information words, removes all non-alphanumeric characters, removes punctuation and converts all uppercase characters to lowercase, and removes all newline and whitespace characters. 


### Interactive analyses 

After pre-processing, the `web.ipynb` file calls in the pre-processed data and uses ipywidgets to create interactive exploratory data analysis and topic modeling via latent dirichlet allocation. In the notebook, we allow the user to choose from the use of two different data sets (full and reduced course syllabi) and three topic modeling approaches (Bag-of-Words; Bi-grams; and Tri-grams). This notebook is the one we containerize via Docker to build an image that we will launch as a website via Google Cloud Platform. 
 
 ## Part 3: Containerization via Docker 
 
 We used Docker along with the Voila software tool to containerize the interactive `web.ipynb` Jupyer Notebook and launch it as a standalone interactive dashboard. We then tagged and pushed this image to DockerHub. The Dockerfile and all other materials and dependencies for building the docker image can be found in the `metadata/docker` folder of the repo. 
 
 ## Part 4: Deployment via Google Cloud Platform 
 
Once we had a working docker image of the interactive dashboard on a publicly available repo (see Part 3), we deployed the image via Google Cloud Platform (GCP) to create a web site that the library planning and assessment team can access and use. To deploy the image via GCP, we used the following steps: 
 
 1. Go to GCP via `https://console.cloud.google.com` Then open the shell/terminal in google cloud platform (called Cloud Shell). To do this, click Activate Cloud Shell at the top by your profile icon. 

2. In the shell, run the docker pull command for the image that you get from DockerHub. 

3. Run `docker images` to get information about the image that you'll need for the next step 

4. Next, run `docker tag` with the name of the image and its info you got from the previous step (e.g., gcr.io/name-of-project)

5. Run `docker push` with the same id information you used in previous step (e.g., gcr.io/name-of-project)

6. Now go to Cloud Run and Create Service and use GUI 

7. Select the container image from the drop-down menu (should be the name you gave it) 

8. Use default location

9. Change service name to image name (or something useful that you can remember)

10. Allow unauthenticated invocations under Authentication (so anyone can make requests and access)

11. Go to additional options (Show additional options)

12. Now change container port to the port the docker image uses (this is the port we expose in the Dockerfile) 

13. Change CPU, Memory allocated, and Maximum requests per container settings as needed to get your app to run smoothly. For this project, we selected the maximum CPU and Memory allocated options. 

14. Now hit Create Now and within a few seconds this will deploy your docker image and create a url that you can copy and share with anyone. 

# CBC Project Information 

```
title: NLP_Syllabi_Project
tags: natural language processing, race, social science 
analysts: Jordan Lawson 
git_repo_url: https://github.com/compbiocore/NLP_Syllabi_Project 
resources_used: Python, Docker, Google Cloud Platform 
summary: An analysis of how racial issues are discussed in courses at Brown 
project_id: 
```


 
 
 
 
 
 