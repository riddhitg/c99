import os
import shutil

#enter the name of the folder to be sorted
path = input("enter the name od the directory to be sorted: ")

#list of all the files and folders in the directory
list_of_files = os.listdir(path)

#go through each and every file
for file in list_of_files:
    name,ext = os.path.splitext(file)

    #store the extension type
    ext = ext[1:]

    #if it is a directory, go to the next loop
    if ext == '':
        continue

    #move the file to the folder name ext  
    if os.path.exists(path + '/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else: 
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)