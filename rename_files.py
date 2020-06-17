# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:01:45 2020

@author: NicNeo
"""

import os 

# ---------- SET CONSTANTS ------------

# NAME OF THE CLASSIFIER
MAIN_NAME = 'cat'

# SUB-FOLDER NAME - CHANGE IF FILE_PATH NAME IS DIFFERENT FROM MAIN_NAME
SUB_PATH = MAIN_NAME

# THE NAME OF YOUR .JPG FILE - CHANGE IF NAME OF .JPG FILE IS DIFFERENT FROM MAIN_NAME
CLASS_NAME = MAIN_NAME

# DON'T EDIT THIS
FILE_PATH = './images/' + SUB_PATH + '/'

# ------------------------------------

# Check current working directory
print(os.getcwd())
  
# Function to rename multiple files 
def rename_files(class_name, file_path): 
    
    '''
        Args:
            -- class_name: rename to the class that this picture is classified
            -- file_path: where to save the final image
    '''
  
    for i, filename in enumerate(os.listdir(file_path)):
        dst_temp = "{}.{}.jpg".format(class_name,i)
        src = file_path + filename 
        dst = file_path + dst_temp
          
        # rename() function will rename all the files
        os.rename(src, dst)
        print("Renamed {} --> {}".format(filename,dst_temp))

rename_files(CLASS_NAME, FILE_PATH)