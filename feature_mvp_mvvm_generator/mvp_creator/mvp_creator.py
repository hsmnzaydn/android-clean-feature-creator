import util.utility as utility
import mvp_creator.mvp_creator_helper as helper


def generatePresenter(presenterName,packageName,viewType):
    utility.createFolder(presenterName.lower())
    genereateContractPart(presenterName,packageName)
    generatePresenterPart(presenterName,packageName)
    #generateModulePart(presenterName,packageName,viewType)
    generateView(presenterName,packageName,viewType)
    manipulateViewInjector(viewType,presenterName)
    aggreatePresenter(presenterName)


def generateView(presenterName,packageName,viewType):
    if viewType == "Fragment":
        utility.createFile(presenterName+"Fragment")
        utility.writeFile(presenterName+"Fragment",helper.generateFragmentViewCode(packageName,presenterName,viewType))
        utility.moveFileToFolder(presenterName+"Fragment",presenterName.lower())
    if viewType == "Activity":   
        utility.createFile(presenterName+"Activity")
        utility.writeFile(presenterName+"Activity",helper.generateActivityViewCode(packageName,presenterName,viewType))
        utility.moveFileToFolder(presenterName+"Activity",presenterName.lower())


def manipulateViewInjector(viewType,presenterName):
    #utility.addCodeToFile("../di/modules/ViewInjectorModules",helper.generateViewInjectorCode(presenterName,viewType))
    utility.addCodeToFile("../di/modules/presenter_module/PresenterModule",helper.generatePresenterInjectorCode(presenterName,viewType))

    
def generateModulePart(presenterName,packageName,viewType):
    utility.createFolder(presenterName.lower()+"_module")
    utility.createFile(presenterName+"Module")
    utility.createFile(presenterName+viewType+"Module")
    utility.writeFile(presenterName+"Module",helper.generatePresenterModuleCode(packageName,presenterName))
    utility.writeFile(presenterName+viewType+"Module",helper.genereateViewModuleCode(packageName,presenterName,viewType))
    utility.moveFileToFolder(presenterName+"Module",presenterName.lower()+"_module")
    utility.moveFileToFolder(presenterName+viewType+"Module",presenterName.lower()+"_module")
    utility.moveFolderToFolder(presenterName.lower()+"_module","../di/modules")


def genereateContractPart(presenterName,packageName):
    utility.createFile(presenterName+"Contract")
    utility.writeFile(presenterName+"Contract",helper.generateContractCode(packageName,presenterName))
    utility.moveFileToFolder(presenterName+"Contract",presenterName.lower())

def generatePresenterPart(presenterName,packageName):
    utility.createFile(presenterName+"Presenter")
    utility.writeFile(presenterName+"Presenter",helper.generatePresenterCode(packageName,presenterName))
    utility.moveFileToFolder(presenterName+"Presenter",presenterName.lower())

def aggreatePresenter(presenterName):
    utility.moveFolderToFolder(presenterName.lower(),"../ui")
