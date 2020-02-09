package com.basefy.testmvp.Home.data.repository

import retrofit2.Retrofit
import com.google.gson.Gson
import com.basefy.testmvp.Home.domain.repository.HomeRepository
import com.basefy.testmvp.ui.base.BaseServicesImp

class HomeRepositoryImpl(private val retrofit:Retrofit,
gson:Gson): BaseServicesImp(retrofit,gson),HomeRepository{

}