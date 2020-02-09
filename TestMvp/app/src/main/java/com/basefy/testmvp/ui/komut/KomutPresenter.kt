package com.basefy.testmvp.ui.komut

import com.basefy.burger_king.ui.base.BasePresenter
import com.basefy.burger_king.ui.base.BaseResponseCallBack
import javax.inject.Inject

class KomutPresenter<V:KomutContract.View> @Inject constructor():
BasePresenter<V>(),KomutContract.Presenter<V>{

}