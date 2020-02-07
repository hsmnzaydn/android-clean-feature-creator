import util.utility as utility
import mvp_creator.mvp_creator_helper as helper


def generatePresenter(presenterName,packageName,viewType):
    utility.createFolder(presenterName.lower())
    genereateContractPart(presenterName,packageName)
    generatePresenterPart(presenterName,packageName)
    generateModulePart(presenterName,packageName,viewType)
    aggreatePresenter(presenterName)



def generateModulePart(presenterName,packageName,viewType):
    utility.createFolder(presenterName.lower()+"_module")
    utility.createFile(presenterName+"Module")
    utility.createFile(presenterName+viewType+"Module")
    utility.writeFile(presenterName+"Module",helper.generatePresenterModuleCode(packageName,presenterName))
    utility.writeFile(presenterName+viewType+"Module",helper.genereateViewModuleCode(packageName,presenterName,viewType))
    utility.moveFileToFolder(presenterName+"Module",presenterName.lower()+"_module")
    utility.moveFileToFolder(presenterName+viewType+"Module",presenterName.lower()+"_module")
    utility.moveFolderToFolder(presenterName.lower()+"_module","./di/modules")

def genereateContractPart(presenterName,packageName):
    utility.createFile(presenterName+"Contract")
    utility.writeFile(presenterName+"Contract",helper.generateContractCode(packageName,presenterName))
    utility.moveFileToFolder(presenterName+"Contract",presenterName)

def generatePresenterPart(presenterName,packageName):
    utility.createFile(presenterName+"Presenter")
    utility.writeFile(presenterName+"Presenter",helper.generatePresenterCode(packageName,presenterName))
    utility.moveFileToFolder(presenterName+"Presenter",presenterName)

def aggreatePresenter(presenterName):
    utility.moveFolderToFolder(presenterName,"./ui")
