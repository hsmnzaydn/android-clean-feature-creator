package com.basefy.testmvp.ui.base



import com.google.gson.Gson
import retrofit2.Retrofit
import javax.inject.Inject


open class BaseServicesImp @Inject constructor(
    private val retrofit: Retrofit,
    private val gson: Gson
)