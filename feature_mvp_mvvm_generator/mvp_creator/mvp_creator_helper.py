

def generateContractCode(packageName,presenterName):
    code = (f"package {packageName}.ui.{presenterName.lower()}\n\n"
            f"import {packageName}.ui.base.MvpPresenter\n"
            f"import {packageName}.ui.base.MvpView\n\n"
            "//TODO: TÜM FONKSİYONLARIN ÜSTÜNE YORUM SATIRI KOYMAYI UNUTMA !!!!\n"
            f"interface {presenterName}Contract"
            "{\n\n"
            "interface View : MvpView {\n\n} \n"
            "interface Presenter<V : View> : MvpPresenter<V> {\n\n}\n}")
    return code

def generatePresenterCode(packageName,presenterName):
    code = (f"package {packageName}.ui.{presenterName.lower()}\n\n"
            f"import {packageName}.ui.base.BasePresenter\n"
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

def generateFragmentViewCode(packageName,presenterName,viewType):

        code = (f"package {packageName}.ui.{presenterName.lower()}\n\n"
                f"import {packageName}.R\n"
                f"import {packageName}.ui.base.BaseFragment\n"
                f"import javax.inject.Inject\n\n"
                f"class {presenterName}Fragment : BaseFragment(),{presenterName}Contract.View \n"
                "{\n"
                "@Inject\n"
                f"lateinit var presenter: {presenterName}Contract.Presenter<{presenterName}Contract.View>\n"
                "private lateinit var root: View\n\n"
                "override fun onCreateView(\n"
                "inflater: LayoutInflater,\n"
                "container: ViewGroup?,\n"
                "savedInstanceState: Bundle?\n"
                "): View? {\n"
                f"root = inflater.inflate(R.layout.fragment_{presenterName.lower()}, container, false)\n"
                "presenter.onAttach(this)\n"
                "return root\n"
                "}\n"
                "}\n")
        return code




def generateActivityViewCode(packageName,presenterName,viewType):

        code = (f"package {packageName}.ui.{presenterName.lower()}\n\n"
                f"import {packageName}.R\n"
                f"import {packageName}.ui.base.BaseActivity\n"
                f"import javax.inject.Inject\n\n"
                f"class {presenterName}Activity : BaseActivity(),{presenterName}Contract.View "
                "{\n"
                "@Inject\n"
                f"lateinit var presenter: {presenterName}Contract.Presenter<{presenterName}Contract.View>\n\n"
                "override fun onCreate(savedInstanceState: Bundle?){\n"
                "super.onCreate(savedInstanceState)\n"
                "setContentView(R.layout.xmlName)\n"
                "presenter.onAttach(this)\n"
                "} }")
        return code


def generateViewInjectorCode(presenterName,viewType):

        code = ("@ActivityScope\n"
                "@ContributesAndroidInjector\n"
                f"abstract fun {presenterName.lower()}{viewType}Injector(): {presenterName}{viewType}\n")
        return code        

def generatePresenterInjectorCode(presenterName,viewType):
        code = ("@Provides\n"
                "@Singleton\n"
                f"fun provide{presenterName}Module(): {presenterName}Contract.Presenter<{presenterName}Contract.View>\n"
                "{\n"
                f"return {presenterName}Presenter()\n"
                "}")
        return code        

