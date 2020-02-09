package com.basefy.testmvp.ui.command

import com.basefy.testmvp.ui.base.MvpPresenter
import com.basefy.testmvp.ui.base.MvpView

interface CommandContract{

interface View : MvpView {

} 
interface Presenter<V : View> : MvpPresenter<V> {
    fun write()

}
}