package com.basefy.testmvp.di.components


import com.basefy.testmvp.TestApp
import com.basefy.testmvp.di.modules.ViewInjectorModules
import com.basefy.testmvp.di.modules.AppModule
import com.basefy.testmvp.di.modules.ServicesModules
import com.basefy.testmvp.di.modules.category_module.CategoryModule
import com.basefy.testmvp.di.modules.komut_module.KomutModule
import com.basefy.testmvp.di.modules.presenter_module.PresenterModule
import dagger.Component
import dagger.android.AndroidInjector
import dagger.android.support.AndroidSupportInjectionModule
import javax.inject.Singleton

@Singleton
@Component(
    modules = [
        AndroidSupportInjectionModule::class,
        AppModule::class,
        ServicesModules::class,
        ViewInjectorModules::class,
        CategoryModule::class,
        PresenterModule::class,
        KomutModule::class
    ]
)
interface ApplicationComponent : AndroidInjector<TestApp> {

    @Component.Builder
    abstract class Builder : AndroidInjector.Builder<TestApp>()

}