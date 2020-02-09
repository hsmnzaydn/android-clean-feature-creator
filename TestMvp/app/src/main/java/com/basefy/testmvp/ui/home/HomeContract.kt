package com.basefy.testmvp.ui.home

import com.basefy.testmvp.ui.base.MvpPresenter
import com.basefy.testmvp.ui.base.MvpView

interface HomeContract {

    interface View : MvpView {

    }

    interface Presenter<V : View> : MvpPresenter<V> {

    }
}