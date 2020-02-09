package com.basefy.testmvp.di.modules.presenter_module

import com.basefy.testmvp.Category.domain.usecases.CategoryUseCase
import com.basefy.testmvp.ui.category.CategoryContract
import com.basefy.testmvp.ui.category.CategoryPresenter
import com.basefy.testmvp.ui.command.CommandContract
import com.basefy.testmvp.ui.command.CommandPresenter
import com.basefy.testmvp.ui.home.HomeContract
import com.basefy.testmvp.ui.home.HomePresenter
import com.basefy.testmvp.ui.komut.KomutContract
import com.basefy.testmvp.ui.komut.KomutPresenter
import dagger.Module
import dagger.Provides
import javax.inject.Singleton

@Module
class PresenterModule {
    @Provides
    @Singleton
    fun provideCategoryModule(categoryUseCase: CategoryUseCase): CategoryContract.Presenter<CategoryContract.View> {
        return CategoryPresenter(categoryUseCase)
    }


    @Provides
    @Singleton
    fun provideCommandModule(categoryUseCase: CategoryUseCase): CommandContract.Presenter<CommandContract.View> {
        return CommandPresenter(categoryUseCase)
    }

    @Provides
    @Singleton
    fun provideHomeModule(): HomeContract.Presenter<HomeContract.View> {
        return HomePresenter()
    }

    @Provides
    @Singleton
    fun provideKomutModule(): KomutContract.Presenter<KomutContract.View> {
        return KomutPresenter()
    }
}
