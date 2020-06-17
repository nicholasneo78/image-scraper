# -*- coding: utf-8 -*-
"""
Created on Sun May 31 20:21:26 2020

@author: NicNeo
"""

# --------- IMPORT LIBRARIES ----------
import pandas as pd
import urllib.request
import os

# ---------- SET CONSTANTS ------------

# INITIAL COUNT OF THE IMAGES
COUNT = 0

# NAME OF THE CLASSIFIER
MAIN_NAME = 'cat'

# SUB-FOLDER NAME - CHANGE IF FILE_PATH NAME IS DIFFERENT FROM MAIN_NAME
SUB_PATH = MAIN_NAME

# DON'T EDIT THIS
FILE_PATH = './images/' + SUB_PATH + '/'

# THE CSV FILE THAT CONTAINS ALL THE LINKS TO THE IMAGES 
# CHANGE IF .CSV FILENAME IS DIFFERENT FROM MAIN_NAME
# MIGHT BE DIFFERENT IF YOU SCRAPED FROM MULTIPLE WEBSITE 
FILENAME = './csv/{}.csv'.format(MAIN_NAME)

# ------------------------------------

# Check current working directory
print(os.getcwd())

# To retrieve photos from the internet
def url_to_jpg(i, url, file_path):
    
    '''
        Args:
            -- i: number of image
            -- url: a URL address of a given image
            -- file_path: where to save the final image
    '''

    filename = 'images-{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url,full_path)
    print('{} saved!'.format(filename))    

# Read List of URLs as pandas dataframe
# error_bad_lines=False for a particular row has more than 1 column,
# causing the error 
urls = pd.read_csv(FILENAME, error_bad_lines=False)

# Track the number of images downloaded
count = COUNT

# Save images to the directory by iterating through the list
for i,url in enumerate(urls.values):
    try:
        if not os.path.exists(FILE_PATH):
            os.mkdir(FILE_PATH)
        url_to_jpg(count, url[0], FILE_PATH)
        count += 1
        #print(url) # TO DEBUG -- Check the link 
    except (KeyboardInterrupt,SystemExit):
        break
    except:
        print("Can't download image!")
        continue