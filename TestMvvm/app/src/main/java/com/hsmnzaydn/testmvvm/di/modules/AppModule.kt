package com.hsmnzaydn.testmvvm.di.modules

import android.content.Context
import com.hsmnzaydn.testmvvm.TestMvvmApp
import dagger.Binds
import dagger.Module

@Module
abstract class AppModule {

    @Binds
    abstract fun provideContext(application: TestMvvmApp): Context
}
