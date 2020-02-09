package com.hsmnzaydn.testmvvm.di.components

import com.hsmnzaydn.testmvvm.TestMvvmApp
import com.hsmnzaydn.testmvvm.di.modules.ViewInjectorModules
import com.hsmnzaydn.testmvvm.di.modules.AppModule
import com.hsmnzaydn.testmvvm.di.modules.NetworkModule
import com.hsmnzaydn.testmvvm.di.modules.ViewModule
import dagger.BindsInstance
import dagger.Component
import dagger.android.support.AndroidSupportInjectionModule
import javax.inject.Singleton

@Singleton
@Component(
    modules = [
        AndroidSupportInjectionModule::class,
        ViewInjectorModules::class,
        AppModule::class,
        NetworkModule::class,
        ViewModule::class
    ]
)
interface ApplicationComponent {
    @Component.Builder
    interface Builder {
        @BindsInstance
        fun application(app: TestMvvmApp): Builder

        fun build(): ApplicationComponent

    }

    fun inject(app: TestMvvmApp)
}