package com.basefy.testmvp.ui.komut

import com.basefy.testmvp.ui.base.MvpPresenter
import com.basefy.testmvp.ui.base.MvpView

interface KomutContract{

interface View : MvpView {

} 
interface Presenter<V : View> : MvpPresenter<V> {

}
}