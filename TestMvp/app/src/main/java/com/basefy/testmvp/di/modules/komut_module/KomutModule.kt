package com.basefy.testmvp.di.modules.komut_module

import com.google.gson.Gson
import com.basefy.testmvp.Komut.data.repository.KomutRepositoryImpl
import com.basefy.testmvp.Komut.domain.repository.KomutRepository
import dagger.Module
import dagger.Provides
import retrofit2.Retrofit
import javax.inject.Singleton


@Module
class KomutModule{

@Provides
@Singleton
fun provideKomutRepository(retrofit: Retrofit, gson: Gson): KomutRepository {
return KomutRepositoryImpl(retrofit,gson)}
}