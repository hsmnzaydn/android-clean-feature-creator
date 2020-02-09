package com.basefy.testmvp.di.modules.home_module

import com.google.gson.Gson
import com.basefy.testmvp.Home.data.repository.HomeRepositoryImpl
import com.basefy.testmvp.Home.domain.repository.HomeRepository
import dagger.Module
import dagger.Provides
import retrofit2.Retrofit
import javax.inject.Singleton


@Module
class HomeModule{

@Provides
@Singleton
fun provideHomeRepository(retrofit: Retrofit, gson: Gson): HomeRepository {
return HomeRepositoryImpl(retrofit,gson)}
}