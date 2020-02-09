package com.hsmnzaydn.testmvvm.di.modules

import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.hsmnzaydn.testmvvm.base.BaseInterfaces
import com.hsmnzaydn.testmvvm.di.ViewModelFactory
import com.hsmnzaydn.testmvvm.di.ViewModelKey
import com.hsmnzaydn.testmvvm.ui.category.CategoryViewModel
import dagger.Binds
import dagger.Module
import dagger.multibindings.IntoMap

@Module
abstract class ViewModule {
    @Binds
    internal abstract fun bindViewModelFactory(factory: ViewModelFactory): ViewModelProvider.Factory


    @Binds
    @IntoMap
    @ViewModelKey(CategoryViewModel::class)
    internal abstract fun categoryViewModel(viewModel: CategoryViewModel<BaseInterfaces>): ViewModel
}