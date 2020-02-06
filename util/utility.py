import os

def writeFile(fileName,code):
    with open(fileName+".kt",'a') as file:
        file.write(code)

def createFile(fileName):
    os.system("touch "+fileName+".kt")

def createFolder(folderName):
    os.system("mkdir "+folderName)

def moveFileToFolder(moveFile,targetFolder):
    os.system("mv "+moveFile+".kt "+targetFolder)

def moveFolderToFolder(moveFolder,targetFolder):
    os.system("mv "+moveFolder+" "+targetFolder)