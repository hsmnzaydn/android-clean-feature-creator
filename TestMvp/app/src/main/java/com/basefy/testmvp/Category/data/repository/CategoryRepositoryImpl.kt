package com.basefy.testmvp.data.repository

import android.util.Log
import retrofit2.Retrofit
import com.google.gson.Gson
import com.basefy.testmvp.Category.domain.repository.CategoryRepository
import com.basefy.testmvp.ui.base.BaseServicesImp
import javax.inject.Inject

class CategoryRepositoryImpl @Inject constructor(
    private val retrofit: Retrofit,
    gson: Gson
) : BaseServicesImp(retrofit, gson), CategoryRepository {
    override fun writeTest() {
        Log.d("veri","veri")
    }

}