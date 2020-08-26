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
    duplicates = list()
    for files in onlyDuplicates.values(): #for each size that has many files
        temp = {}
        for f in files: #for each file of that size
            temp[f] = hashFile(f) #get hash of that file
        rev_temp ={}
        for fileN, hashvalue in temp.items(): #reverse the dict to group by hash value
            rev_temp.setdefault(hashvalue, set()).add(fileN)
        for files in rev_temp.values():
            if (len(files) > 1): #only add files that have identical hashes
                duplicates.append(files)   
    return duplicates

#open file and perform md5 hash
def hashFile(fileName):
    buffer_size = 65536 

    hasher = hashlib.md5()
    with open(fileName, 'rb') as fi:
        while True:
            data =fi.read(buffer_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

#formatting of output
def printDuplicates(duplicates):
    for group in duplicates:
        print("These files are duplicates:\n")
        for f in group:
            print(f)
        print("\n")    



def main():
    dirName =input("Please enter the full path of directory to search: ")

    while not(os.path.isdir(dirName)):
        dirName = input("Please enter a valid directory: ")

    allfile = getAllFiles(dirName)
    grouped = groupDuplicateSize(allfile)
    duplicates = searchRealDuplicates(grouped)
    printDuplicates(duplicates)


if __name__ == "__main__":
    main()