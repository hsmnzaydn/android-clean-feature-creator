

def generateViewModelCode(packageName,viewmodelname):
    code = (f"package {packageName}.ui.{viewmodelname.lower()}\n\n"
    f"import {packageName}.base.BaseInterfaces\n"
    f"import {packageName}.base.BaseResponseCallBack\n"
    f"import {packageName}.base.BaseViewModel\n"
    "import javax.inject.Inject\n"
    f"class {viewmodelname}ViewModel<I : BaseInterfaces> @Inject constructor(): \n"
    "BaseViewModel<I>(){\n\n }")

    return code

def generateViewActivityCode(packageName,viewmodelname,viewType):
    code = (f"package {packageName}.ui.{viewmodelname.lower()}\n\n"
            "import android.os.Bundle\n"
            "import androidx.lifecycle.Observer\n"
            f"import {packageName}.ui.{viewmodelname.lower()}.{viewmodelname}ViewModel\n"
            f"import {packageName}.R\n"
            f"import {packageName}.base.BaseActivity\n"
            f"import {packageName}.base.BaseFragment\n"
            f"import {packageName}.base.BaseInterfaces\n"
            f"import {packageName}.databinding.{viewType}{viewmodelname}Binding\n\n"
            f"class {viewmodelname}{viewType} : BaseActivity<{viewType}{viewmodelname}Binding, {viewmodelname}ViewModel<BaseInterfaces>>()\n"
            "{\n\n"
            "override fun layoutRes(): Int = R.layout.layoutName\n"
            f"override fun model() = {viewmodelname}ViewModel::class.java\n"
            "}")

    return code


def generateViewInjectorViewModelCode(viewmodelName,viewType):
    code = ("@ContributesAndroidInjector\n"
            f"abstract fun {viewmodelName.lower()}{viewType}Injector(): {viewmodelName}{viewType}\n")
    return code

def generateViewModelInjectorCode(viewmodelName,viewType):
    code = ("@Binds\n"
            "@IntoMap\n"
            f"@ViewModelKey({viewmodelName}ViewModel::class)\n"
            f"internal abstract fun {viewmodelName.lower()}ViewModel(viewModel: {viewmodelName}ViewModel<BaseInterfaces>): ViewModel")
    return code        