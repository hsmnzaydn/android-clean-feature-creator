import util.utility as utility
import mvvm_creator.mvvm_creator_helper as helper

def generateViewModel(viewmodelName,packageName,viewType):
    utility.createFolder(viewmodelName.lower())
    generateViewModelPart(viewmodelName,packageName)
    generateView(viewmodelName,packageName,viewType)
    aggreateViewModel(viewmodelName)
    manipulateViewInjector(viewType,viewmodelName)

def manipulateViewInjector(viewType,viewmodelName):
    utility.addCodeToFile("../di/modules/ViewInjectorModules",helper.generateViewInjectorViewModelCode(viewmodelName,viewType))
    utility.addCodeToFile("../di/modules/ViewModule",helper.generateViewModelInjectorCode(viewmodelName,viewType))


def generateView(viewmodelName,packageName,viewType):
    if viewType == "Fragment":
        utility.createFile(viewmodelName+"Fragment")
        utility.writeFile(viewmodelName+"Fragment",helper.generateViewActivityCode(packageName,viewmodelName,viewType))
        utility.moveFileToFolder(viewmodelName+"Fragment",viewmodelName.lower())
    if viewType == "Activity":   
        utility.createFile(viewmodelName+"Activity")
        utility.writeFile(viewmodelName+"Activity",helper.generateViewActivityCode(packageName,viewmodelName,viewType))
        utility.moveFileToFolder(viewmodelName+"Activity",viewmodelName.lower())

def generateViewModelPart(viewmodelName,packageName):
    utility.createFile(viewmodelName+"ViewModel")
    utility.writeFile(viewmodelName+"ViewModel",helper.generateViewModelCode(packageName,viewmodelName))
    utility.moveFileToFolder(viewmodelName+"ViewModel",viewmodelName.lower())

def aggreateViewModel(viewmodelName):
    utility.moveFolderToFolder(viewmodelName.lower(),"../ui")