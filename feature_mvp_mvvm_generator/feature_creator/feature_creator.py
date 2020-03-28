import os
import util.utility as utility
import feature_creator.feature_creator_helper as helper 

def generateFeature(packageName, featureName): 
   utility.createFolder(featureName)
   repositoryName = featureName+"Repository"
   repositoryImpName= featureName+"RepositoryImpl" 
   generateDataLayer(packageName,featureName,repositoryName,repositoryImpName)
   generateDomainLayer(repositoryName,packageName,featureName)
   aggreateFeature(featureName)
   generateModuleLayer(packageName,featureName,repositoryName,repositoryImpName)

def aggreateFeature(featureName):
    utility.moveFolderToFolder("domain",featureName)
    utility.moveFolderToFolder("data",featureName)
    utility.moveFolderToFolder(featureName,"../")


#MODULE CREATOR
def generateModuleLayer(packageName,featureName,repositoryName,repositoryImpName):
    utility.createFolder(featureName.lower()+"_module")
    utility.createFile(featureName+"Module")
    utility.writeFile(featureName+"Module",helper.generateModuleCode(packageName,featureName,repositoryName,repositoryImpName))
    utility.moveFileToFolder(featureName+"Module",featureName.lower()+"_module")
    utility.moveFolderToFolder(featureName.lower()+"_module","../di/modules")



#DOMAIN CREATOR
def generateDomainLayer(repositoryName,packageName,featureName):
    utility.createFolder("domain")
    generateDomainMapper(featureName)
    generateDomainEntity()
    generateDomainRepository(repositoryName,packageName,featureName)
    generateUseCases(packageName,repositoryName,featureName)
    aggreateDomain()

def generateDomainEntity():    
    utility.createFolder("entities")

def generateDomainMapper(featureName):
    utility.createFolder("mapper")
    utility.createFile(featureName+"Mapper")
    utility.moveFileToFolder(featureName+"Mapper","mapper")

def generateDomainRepository(repositoryName,packageName,featureName):
    utility.createFolder("repository")
    utility.createFile(featureName+"Repository")
    utility.writeFile(repositoryName,helper.generateRepositoryCode(packageName,featureName,repositoryName))
    utility.moveFileToFolder(repositoryName,"repository")

def aggreateDomain():
    utility.moveFolderToFolder("entities","domain")
    utility.moveFolderToFolder("mapper","domain")
    utility.moveFolderToFolder("repository","domain")
    utility.moveFolderToFolder("usecase","domain")

def generateUseCases(basePackage,repositoryName,featureName):
    utility.createFile(featureName+"UseCase")
    utility.createFolder("usecase")
    utility.writeFile(featureName+"UseCase",helper.generateUseCaseCode(basePackage,featureName,repositoryName))
    utility.moveFileToFolder(featureName+"UseCase","usecase")

#DATA CREATOR    
def generateDataLayer(packageName,featureName,repositoryName,repositoryImpName):
    utility.createFolder("data")

    generateEntitiesPart()
    generateApiPart(packageName,featureName)
    generateRepositoryPart(packageName,featureName,repositoryName,repositoryImpName)
    aggreateData(featureName)

def aggreateData(featureName):
    utility.moveFolderToFolder("api","data")
    utility.moveFolderToFolder("repository","data")
    utility.moveFolderToFolder("entities","data")
    utility.moveFolderToFolder("data",featureName)


def generateApiPart(packageName,featureName):
    utility.createFolder("api")
    serviceFileName= featureName + "Services"
    utility.createFile(serviceFileName)
    utility.writeFile(serviceFileName,helper.generateApiCode(serviceFileName,packageName,featureName))
    utility.moveFileToFolder(serviceFileName,"api")

    
def generateEntitiesPart():
    utility.createFolder("entities")

def generateRepositoryPart(packageName,featureName,repositoryName,repositoryImpName):
    utility.createFolder("repository")
    utility.createFile(repositoryImpName)
    utility.writeFile(repositoryImpName,helper.generateRepositoryImpCode(packageName,featureName,repositoryName,repositoryImpName))
    utility.moveFileToFolder(repositoryImpName,"repository")

