package com.hsmnzaydn.testmvvm.di.modules

import android.content.Context
import com.google.gson.Gson
import dagger.Module
import dagger.Provides
import okhttp3.*
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory
import retrofit2.converter.gson.GsonConverterFactory
import javax.inject.Singleton

@Module
class NetworkModule {

    @Singleton
    @Provides
    fun provideGson(): Gson = Gson()

    @Provides
    @Singleton
    fun provideRetrofitClient(context: Context): Retrofit {
        val cacheSize = 10 * 1024 * 1024
        val cache = Cache(context.cacheDir, cacheSize.toLong())

        val loggingInterceptor = HttpLoggingInterceptor()
        loggingInterceptor.level = HttpLoggingInterceptor.Level.BODY
        val okHttpClient = OkHttpClient.Builder()

            .cache(cache)

            .addInterceptor(object : Interceptor {
                override fun intercept(chain: Interceptor.Chain): Response {

                    var request: Request =
                        chain.request().newBuilder()
                            .addHeader("Accept", "/")
                            .addHeader("Accept-Encoding", "gzip, deflate")
                            .addHeader("User-Agent", "runscope/0.1")
                            .addHeader("Content-Type", "application/json")
                            .addHeader("Language", "TR")
                            .build()

                    return chain.proceed(request)
                }

            })
            .addInterceptor(loggingInterceptor)
            .build()


        return Retrofit.Builder().baseUrl("").client(okHttpClient)
            .addConverterFactory(GsonConverterFactory.create())
            .addCallAdapterFactory(RxJava2CallAdapterFactory.create()).build()

    }




}
