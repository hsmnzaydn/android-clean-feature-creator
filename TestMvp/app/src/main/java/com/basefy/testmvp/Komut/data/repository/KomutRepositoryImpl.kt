package com.basefy.testmvp.Komut.data.repository

import retrofit2.Retrofit
import com.google.gson.Gson
import com.basefy.base_mvvm_libraries.network.BaseServicesImp
import com.basefy.testmvp.Komut.domain.repository.KomutRepository

class KomutRepositoryImpl(private val retrofit:Retrofit,
gson:Gson):BaseServicesImp(retrofit,gson),KomutRepository{

}