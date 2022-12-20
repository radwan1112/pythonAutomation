# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 10:10:43 2022

@author: radwan alshawesh
"""


import glob
import os
import shutil


src_folder = r"D:\study\python\automation\moving_files\data\images"

train_cat_dst_folder = r"D:\study\python\automation\moving_files\data\train\cat"
val_cat_dst_folder = r"D:\study\python\automation\moving_files\data\val\cat"
train_dog_dst_folder = r"D:\study\python\automation\moving_files\data\train\dog"
val_dog_dst_folder = r"D:\study\python\automation\moving_files\data\val\dog"

#move file whose name starts with string "cat"

pattern_cat = src_folder + "\cat*"
pattern_dog = src_folder + "\dog*"


for file in glob.iglob(pattern_cat, recursive=True):
    # Extract file name from file path
    file_name = os.path.basename(file)
    train_cat_files = os.listdir(train_cat_dst_folder)
    val_cat_files = os.listdir(val_cat_dst_folder)
    no_of_train_cat_files = len(train_cat_files)
    no_of_val_cat_files = len(val_cat_files)
    
    if(no_of_train_cat_files < 6):
        shutil.move(file, train_cat_dst_folder)
        print('Moved: ', file)
    elif(no_of_val_cat_files < 6):
        shutil.move(file, val_cat_dst_folder)
        print('Moved: ', file)
        
for file in glob.iglob(pattern_dog, recursive=True):
    # Extract file name from file path
    file_name = os.path.basename(file)
    train_dog_files = os.listdir(train_dog_dst_folder)
    val_dog_files = os.listdir(val_dog_dst_folder)
    no_of_train_dog_files = len(train_dog_files)
    no_of_val_dog_files = len(val_dog_files)
    
    if(no_of_train_dog_files < 6):
        shutil.move(file, train_dog_dst_folder)
        print('Moved: ', file)
    elif(no_of_val_dog_files < 6):
        shutil.move(file, val_dog_dst_folder)
        print('Moved: ', file)