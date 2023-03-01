import os
import pandas as pd
import numpy as np

def convert_chapters(access_folder_path: str, name_for_saved_file:str):
    folder_path = access_folder_path
    df = pd.DataFrame({'Title': [], 'Text': []})
    titles = []
    texts =[]
    # loop through all files in the folder
    #for filename in os.listdir(folder_path):
    # check if the file is a text file
    #if filename.endswith('.txt'):
    for filename in os.listdir(folder_path):
    # check if the file is a text file
        with open(folder_path+filename,'r',encoding="utf8") as file:
            lines = [line.rstrip() for line in file]
            titles.append(lines[0])
            lines = " ".join(lines[1:])
            texts.append(lines)

    df["Title"] = titles
    df["Text"] = texts
    df.to_csv(name_for_saved_file + '.csv', index=False)

def convert_articles(access_folder_path: str, name_for_saved_file:str):
    folder_path = access_folder_path
    df = pd.DataFrame({'Title': [], 'Text': []})
    titles = []
    texts =[]
    # loop through all files in the folder
    #for filename in os.listdir(folder_path):
    # check if the file is a text file
    #if filename.endswith('.txt'):
    for filename in os.listdir(folder_path):
    # check if the file is a text file
        with open(folder_path+filename,'r',encoding="utf8") as file:
            lines = [line.rstrip() for line in file]
            title = "Article " + lines[0].split()[0]
            titles.append(title)
            text = " ".join(lines[0].split()[1:]) + ". " + " ".join(lines[1:])
            texts.append(text)

    df["Title"] = titles
    df["Text"] = texts
    df.to_csv(name_for_saved_file + '.csv', index=False)

convert_chapters("E:/Useable Data/New folder/", "Chapters")
convert_articles("E:/Useable Data/Annexures/Articles/", "Articles")
    
