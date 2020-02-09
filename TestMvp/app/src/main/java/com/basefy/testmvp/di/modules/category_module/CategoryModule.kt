package com.basefy.testmvp.di.modules.category_module

import com.google.gson.Gson
import com.basefy.testmvp.Category.domain.repository.CategoryRepository
import com.basefy.testmvp.data.repository.CategoryRepositoryImpl
import dagger.Module
import dagger.Provides
import retrofit2.Retrofit
import javax.inject.Singleton


@Module
class CategoryModule {

    @Provides
    @Singleton
    fun provideCategoryRepository(retrofit: Retrofit, gson: Gson): CategoryRepository {
        return CategoryRepositoryImpl(retrofit, gson)
    }
}