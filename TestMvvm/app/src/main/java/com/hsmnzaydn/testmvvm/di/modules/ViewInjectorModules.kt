package com.hsmnzaydn.testmvvm.di.modules

import com.hsmnzaydn.testmvvm.ui.category.CategoryActivity
import dagger.Module
import dagger.android.ContributesAndroidInjector


@Module
abstract class ViewInjectorModules {


@ContributesAndroidInjector
abstract fun categoryActivityInjector(): CategoryActivity

}
