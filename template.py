import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')


project_name="TextSummarizer"

list_of_files=[
    "github/workflows/.gitkeep",## its a completley hidden file so that git file doesnt reamins empty
    f"src/{project_name}/_init_.py",##init.py is a constructor file so that import file in which local file becomes a package 
    ##A constructor is the method that is automatically called when a new instance of a class is created.
    f"src/{project_name}/components/_init_.py",         # Initializes the 'components' module
    f"src/{project_name}/utils/_init_.py", # where utils a folder inside the component  # Initializes the 'utils' module inside 'components'
    f"src/{project_name}/utils/common.py", # inside this common file we have the utility # Contains utility functions or classes, in 'utils' folder
    f"src/{project_name}/logging//init_.py", # Initializes the 'logging' module
    f"src/{project_name}/config/init_.py", # Initializes the 'config' module
    f"src/{project_name}/config/configuration.py", # Contains configurations, in 'config' folder
    f"src/{project_name}/pipeline/init_.py", # Initializes the 'pipeline' module
    f"src/{project_name}/pipeline/init_.py", # Initializes the 'entity' module
    f"src/{project_name}/entity/init_.py", #Initializes the 'constants' module
    f"src/{project_name}/constants/init_.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt"
    "setup.py",
    "research/trials.ipynb" #It will have all the notebook experminets itself
    # basic template creation

]
for filepath in list_of_files : #it means we are looking into this files
    filepath=Path(filepath) #it will take a look at operating system because linux requires forward slash whereas windows require forward slash
    # so it basically adjust the path according to library pathlib
    filedir,filename=os.path.split(filepath)
    # since we are having file and folders together so we are seprating them and creating a hierarchy
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
        # we are checking if this directory is empty there is no sense of running this logic so we are making sure its not empty so we can run the logic

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):    # here we are checking the file size if thats 0 create a file
       with open(filepath,'w') as f:
         pass
         logging.info(f"Creating empty file:{filepath}")



    else:
        logging.info(f"{filename} is already exists ")     
