package com.basefy.testmvp



import com.basefy.testmvp.di.components.DaggerApplicationComponent
import dagger.android.AndroidInjector
import dagger.android.DaggerApplication


class TestApp : DaggerApplication() {

    private val appComponent: AndroidInjector<TestApp> by lazy {
        DaggerApplicationComponent
            .builder()
            .create(this)
    }

    override fun applicationInjector(): AndroidInjector<out DaggerApplication> {
        return appComponent
    }


}
