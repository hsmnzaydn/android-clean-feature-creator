package com.basefy.burger_king.ui.base


import com.basefy.testmvp.ui.base.MvpPresenter
import com.basefy.testmvp.ui.base.MvpView


open class BasePresenter<V : MvpView>
constructor() : MvpPresenter<V> {

    lateinit var mvpView: V



    override fun onAttach(mvpView: V) {
        this.mvpView = mvpView
    }
}

