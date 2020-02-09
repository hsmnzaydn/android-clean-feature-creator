package com.basefy.testmvp.ui.category

import com.basefy.testmvp.ui.base.MvpPresenter
import com.basefy.testmvp.ui.base.MvpView

interface CategoryContract{

interface View : MvpView {

} 
interface Presenter<V : View> : MvpPresenter<V> {

}
}