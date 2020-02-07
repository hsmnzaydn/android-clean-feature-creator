

def generateContractCode(packageName,presenterName):
    code = (f"package {packageName}.ui.{presenterName.lower()}\n\n"
            f"import {packageName}.ui.base.MvpPresenter\n"
            f"import {packageName}.ui.base.MvpView\n\n"
            f"interface {presenterName}Contract"
            "{\n\n"
            "interface View : MvpView {\n\n} \n"
            "interface Presenter<V : View> : MvpPresenter<V> {\n\n}\n}")
    return code

def generatePresenterCode(packageName,presenterName):
    code = (f"package {packageName}.ui.{presenterName.lower()}\n\n"
            f"import com.basefy.burger_king.ui.base.BasePresenter\n"
            "import com.basefy.burger_king.ui.base.BaseResponseCallBack\n"
            "import javax.inject.Inject\n\n"
            f"class {presenterName}Presenter<V:{presenterName}Contract.View> @Inject constructor():\n"
            f"BasePresenter<V>(),{presenterName}Contract.Presenter<V>"
            "{\n\n}")
    return code

def generatePresenterModuleCode(packageName,presenterName):
    code = (f"package {packageName}.di.modules.{presenterName.lower()}_module\n\n"
            f"import {packageName}.scopes.ActivityScope\n"
            f"import {packageName}.ui.{presenterName.lower()}.{presenterName}Contract\n"
            f"import {packageName}.ui.{presenterName.lower()}.{presenterName}Presenter\n"
            "import dagger.Module\n"
            "import dagger.Provides\n\n\n"
            "@Module\n"
            f"class {presenterName}Module"
            "{\n"
            "@ActivityScope\n"
            "@Provides\n"
            f"fun presenter():{presenterName}Contract.Presenter<{presenterName}Contract.View> =\n"
            f"{presenterName}Presenter()\n"
            "}")
    return code

def genereateViewModuleCode(packageName,presenterName,viewType):

    code = (f"package {packageName}.di.modules.{presenterName.lower()}_module\n\n"
            f"import {packageName}.di.scopes.ActivityScope\n"
            f"import {packageName}.ui.{presenterName.lower()}.{presenterName}{viewType}\n"
            f"import dagger.Module\n"
            f"import dagger.android.ContributesAndroidInjector\n\n"
            "@Module\n"
            f"abstract class {presenterName}{viewType}Module"
            "{\n\n"
            "@ActivityScope\n"
            f"@ContributesAndroidInjector(modules= [{presenterName}Module::class])\n"
            f"internal abstract fun contribute{presenterName}{viewType}Injector():{presenterName}{viewType}\n"
            "}")
    return code


