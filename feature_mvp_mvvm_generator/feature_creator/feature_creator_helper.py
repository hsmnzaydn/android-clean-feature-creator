import os

def generateApiCode(serviceFileName,basePackage,featureName):
    code = (f"package {basePackage}.{featureName}.data.api \n\n\n"
            f"interface {serviceFileName} "
            "{\n\n}")
    return code

def generateRepositoryImpCode(basePackage,featureName,repositoryName,repositoryImplName):
    code = (f"package {basePackage}.{featureName}.data.repository\n\n"
            f"import retrofit2.Retrofit\n"
            f"import {basePackage}.{featureName}.domain.repository.{featureName}Repository\n\n"
            f"class {repositoryImplName}(private val retrofit:Retrofit):BaseServicesImp(retrofit),{repositoryName}"
            "{\n"
            f"fun get{featureName}Services(): {featureName}Services = retrofit.create({featureName}Services::class.java)\n"
            "\n}")
    return code

def generateRepositoryCode(basePackage,featureName,repositoryName):
    code = (f"package {basePackage}.{featureName}.domain.repository\n\n"
            f"interface {featureName}Repository"
            "{\n\n}")
    return code        
    
def generateUseCaseCode(basePackage,featureName,repositoryName):
    
    code = (f"package {basePackage}.{featureName}.domain.usecase\n\n"
            f"import {basePackage}.{featureName}.domain.repository.{featureName}Repository\n"
            "import javax.inject.Inject\n\n"
            "//TODO: TÜM FONKSİYONLARIN ÜSTÜNE YORUM SATIRI KOYMAYI UNUTMA !!!!\n"
            f"class {featureName}UseCase @Inject constructor(private val {featureName.lower()}Repository: {featureName}Repository)"
            "{\n\n}")
    return code

def generateModuleCode(basePackage,featureName,repositoryName,repositoryImplName):
        code = (f"package {basePackage}.di.modules.{featureName.lower()}_module\n\n"
                f"import {basePackage}.{featureName}.data.repository.{repositoryImplName}\n"
                f"import {basePackage}.{featureName}.domain.repository.{repositoryName}\n"
                "import dagger.Module\n"
                "import dagger.Provides\n"
                "import dagger.hilt.InstallIn\n"
                "import retrofit2.Retrofit\n"
                "import dagger.hilt.components.SingletonComponent\n"
                "import javax.inject.Singleton\n\n\n"
                "@Module\n"
                "@InstallIn(SingletonComponent::class)\n"
                f"class {featureName}Module"
                "{\n\n"
                "@Provides\n"
                "@Singleton\n"
                f"fun provide{repositoryName}(retrofit: Retrofit): {repositoryName} "
                "{\n"
                f"return {repositoryImplName}(retrofit)"
                "}\n"
                "}")
        return code        
