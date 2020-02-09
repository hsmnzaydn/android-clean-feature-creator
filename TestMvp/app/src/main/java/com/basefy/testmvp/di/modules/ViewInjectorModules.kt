package com.basefy.testmvp.di.modules


import com.basefy.testmvp.di.scopes.ActivityScope
import com.basefy.testmvp.ui.category.CategoryActivity
import com.basefy.testmvp.ui.command.CommandActivity
import com.basefy.testmvp.ui.home.HomeActivity
import com.basefy.testmvp.ui.komut.KomutActivity
import dagger.Module
import dagger.android.ContributesAndroidInjector

@Module
abstract class ViewInjectorModules {

    @ActivityScope
    @ContributesAndroidInjector
    abstract fun categoryActivityInjector(): CategoryActivity

    @ActivityScope
    @ContributesAndroidInjector
    abstract fun commandActivityInjector(): CommandActivity

    @ActivityScope
    @ContributesAndroidInjector
    abstract fun homeActivityInjector(): HomeActivity

    @ActivityScope
    @ContributesAndroidInjector
    abstract fun komutActivityInjector(): KomutActivity

}
