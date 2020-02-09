package com.basefy.testmvp.di.modules

import android.content.Context
import com.basefy.testmvp.TestApp
import dagger.Binds
import dagger.Module

@Module
abstract class AppModule {
    @Binds
    abstract fun provideContext(application: TestApp): Context
}
