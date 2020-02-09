package com.basefy.testmvp.ui.base

interface MvpPresenter<V : MvpView> {
    fun onAttach(mvpView: V)
}
