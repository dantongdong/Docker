import sys
import os

sys.stdout = open("fileList.txt", "w")
fileNames = ["Data/Hugo", "Data/shakespeare", "Data/Tolstoy"]
for fileName in fileNames:
    index = len(fileName) - len(fileName.split("/")[-1])
    for root, dirs, files in os.walk(fileName, topdown=True):
        parsed_root = root[index:]
        for file in files:
            filePath = 'Data/' + parsed_root + '/' + file
            print(filePath)
sys.stdout.close()
sys.stdout = sys.__stdout__