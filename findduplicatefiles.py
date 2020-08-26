import hashlib
import os
import sys


# make a dict with key-value path-file size
def getAllFiles(dirName):
    allFiles = {}
    for root, dirs, files in os.walk(dirName):
        for file in files:
            allFiles[os.path.join(root, file)] = os.path.getsize(os.path.join(root, file)) #path is key, size (in bytes) is value
    return allFiles        


def groupDuplicateSize(allFiles):
    #1st group duplicates
    rev_dict = {}
    for key, value in allFiles.items():
        rev_dict.setdefault(value, set()).add(key)
    #remove unique values    
    onlyDuplicates = {}
    for key, values in rev_dict.items():
        if (len(values) > 1):
            onlyDuplicates[key] = values
    return onlyDuplicates        

#use hashing to compare files with identical sizes
def searchRealDuplicates(onlyDuplicates):
    #WRITE SOME CODE HERE
    return 0

def hashFile(fileName):
    buffer_size = 65536 #is this good idk?




def main():
    dirName ='/Users/emilia/Documents/learningpython/testingDuplicates'
    allfile = getAllFiles(dirName)
    # for elem in allfile:
    #     print(elem)

    print(allfile)

    grouped = groupDuplicateSize(allfile)

    print(grouped)
    


if __name__ == "__main__":
    main()