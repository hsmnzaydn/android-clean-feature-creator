

def generateContractCode(packageName,presenterName):
    code = (f"package {packageName}.ui.{presenterName.lower()}\n"
            f"import {packageName}.base.MvpPresenter\n"
            f"import {packageName}.base.MvpView\n\n"
            "//TODO: TÜM FONKSİYONLARIN ÜSTÜNE YORUM SATIRI KOYMAYI UNUTMA !!!!\n"
            f"interface {presenterName}Contract"
            "{\n\n"
            "interface View : MvpView {\n\n} \n"
            "interface Presenter<V : View> : MvpPresenter<V> {\n\n}\n}")
    return code

def generatePresenterCode(packageName,presenterName):
    code = (f"package {packageName}.ui.{presenterName.lower()}\n\n"
            f"import {packageName}.base.BasePresenter\n"
            "import javax.inject.Inject\n\n"
            f"class {presenterName}Presenter<V:{presenterName}Contract.View> @Inject constructor():\n"
            f"BasePresenter<V>(),{presenterName}Contract.Presenter<V>"
            "{\n\n}")
    return code

def generatePresenterModuleCode(packageName,presenterName):
    code = (f"package {packageName}.di.modules.{presenterName.lower()}_module\n\n"
            f"import {packageName}.scopes.ActivityScope\n"
            f"import {packageName}.ui.{presenterName.lower()}.{presenterName}Contract\n"
            "import dagger.hilt.components.SingletonComponent\n"
            f"import {packageName}.ui.{presenterName.lower()}.{presenterName}Presenter\n"
            "import dagger.Module\n"
            "import dagger.Provides\n\n\n"
            "@Module\n"
            "@InstallIn(SingletonComponent::class)\n"
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
                f"import {packageName}.base.BaseFragment\n"
                "import dagger.hilt.android.AndroidEntryPoint\n"
                f"import javax.inject.Inject\n\n"
                "@AndroidEntryPoint\n"
                f"class {presenterName}Fragment : BaseFragment<{viewType}{presenterName}Binding>(),{presenterName}Contract.View \n"
                "{\n"
                "@Inject\n"
                f"lateinit var presenter: {presenterName}Contract.Presenter<{presenterName}Contract.View>\n"
                "override fun initUI(){\n"
                f"binding = {viewType}{presenterName}Binding.inflate(layoutInflater)\n"
                "presenter.onAttach(this)\n"
                "}\n"
                "override fun againOpened(){\n}"
                "}\n")
        return code




def generateActivityViewCode(packageName,presenterName,viewType):

        code = (f"package {packageName}.ui.{presenterName.lower()}\n\n"
                f"import {packageName}.R\n"
                f"import {packageName}.base.BaseActivity\n"
                "import dagger.hilt.android.AndroidEntryPoint\n"
                f"import javax.inject.Inject\n\n"
                "@AndroidEntryPoint\n"
                f"class {presenterName}Activity : BaseActivity(),{presenterName}Contract.View "
                "{\n"
                "@Inject\n"
                f"lateinit var presenter: {presenterName}Contract.Presenter<{presenterName}Contract.View>\n"
                f"private lateinit var binding:{viewType}{presenterName}Binding\n\n"
                "override fun onCreate(savedInstanceState: Bundle?){\n"
                "super.onCreate(savedInstanceState)\n"
                f"binding = {viewType}{presenterName}Binding.inflate(layoutInflater)\n"
                "setContentView(binding.root)\n"
                "presenter.onAttach(this)\n"
                "} }")
        return code



def generatePresenterInjectorCode(presenterName,viewType):
        code = ("@Provides\n"
                "@Singleton\n"
                f"fun provide{presenterName}Module(): {presenterName}Contract.Presenter<{presenterName}Contract.View>\n"
                "{\n"
                f"return {presenterName}Presenter()\n"
                "}")
        return code        

