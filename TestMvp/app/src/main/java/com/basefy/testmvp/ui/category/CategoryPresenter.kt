package com.basefy.testmvp.ui.category

import com.basefy.burger_king.ui.base.BasePresenter
import com.basefy.burger_king.ui.base.BaseResponseCallBack
import com.basefy.testmvp.Category.domain.usecases.CategoryUseCase
import javax.inject.Inject

class CategoryPresenter<V : CategoryContract.View> @Inject constructor(categoryUseCase: CategoryUseCase) :
    BasePresenter<V>(), CategoryContract.Presenter<V> {

}