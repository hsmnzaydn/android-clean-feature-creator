package com.basefy.testmvp.ui.home

import com.basefy.burger_king.ui.base.BasePresenter
import com.basefy.burger_king.ui.base.BaseResponseCallBack
import javax.inject.Inject

class HomePresenter<V:HomeContract.View> @Inject constructor():
BasePresenter<V>(),HomeContract.Presenter<V>{

}