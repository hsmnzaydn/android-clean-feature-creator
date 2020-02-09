package com.basefy.testmvp.ui.command

import com.basefy.burger_king.ui.base.BasePresenter
import com.basefy.burger_king.ui.base.BaseResponseCallBack
import com.basefy.testmvp.Category.domain.usecases.CategoryUseCase
import javax.inject.Inject

class CommandPresenter<V:CommandContract.View> @Inject constructor(private val categoryUseCase: CategoryUseCase):
BasePresenter<V>(),CommandContract.Presenter<V>{
    override fun write() {
        categoryUseCase.writeCode()
    }

}