import os

def generateApiCode(serviceFileName,basePackage,featureName):
    code = (f"package {basePackage}.data.api \n\n\n"
            f"interface {serviceFileName} "
            "{\n\n}")
    return code

def generateRepositoryImpCode(basePackage,featureName,repositoryName,repositoryImplName):
    code = (f"package {basePackage}.data.repository\n\n"
            f"import retrofit2.Retrofit\n"
            "import com.google.gson.Gson\n"
            "import com.basefy.base_mvvm_libraries.network.BaseServicesImp\n"
            f"import {basePackage}.{featureName}.domain.repository.{featureName}Repository\n\n"
            f"class {repositoryImplName}(private val retrofit:Retrofit,\ngson:Gson):BaseServicesImp(retrofit,gson),{repositoryName}"
            "{\n\n}")
    return code

def generateRepositoryCode(basePackage,featureName,repositoryName):
    code = (f"package {basePackage}.{featureName}.domain.repository\n\n"
            f"interface {featureName}Repository"
            "{\n\n}")
    return code        
    
def generateUseCaseCode(basePackage,featureName,repositoryName):
    
    code = (f"package {basePackage}.{featureName}.domain.usecases\n\n"
            f"import com.basefy.base_mvvm_libraries.network.BaseServiceCallback\n"
            f"import {basePackage}.{featureName}.domain.repository.{featureName}Repository\n"
            f"import {basePackage}.base.BaseResponseCallback\n"
            "import javax.inject.Inject\n\n"
            f"class {featureName}UseCase @Inject constructor(private val {featureName.lower()}Repository: {featureName}Repository)"
            "{\n\n}")
    return code

def generateModuleCode(basePackage,featureName,repositoryName,repositoryImplName):
        code = (f"package {basePackage}.di.modules.{featureName.lower()}\n\n"
                f"import com.google.gson.Gson\n"
                f"import {basePackage}.{featureName}.data.repository.{repositoryImplName}\n"
                f"import {basePackage}.{featureName}.domain.repository.{repositoryName}\n"
                "import dagger.Module\n"
                "import dagger.Provides\n"
                "import retrofit2.Retrofit\n"
                "import javax.inject.Singleton\n\n\n"
                "@Module\n"
                f"class {featureName}Module"
                "{\n\n"
                "@Provides\n"
                "@Singleton\n"
                f"fun provide{repositoryName}(retrofit: Retrofit, gson: Gson): {repositoryName} "
                "{\n"
                f"return {repositoryImplName}(retrofit,gson)"
                "}\n"
                "}")
        return code        
