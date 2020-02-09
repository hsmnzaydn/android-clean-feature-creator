package com.basefy.testmvp.ui.category

import android.os.Bundle
import com.basefy.testmvp.R
import com.basefy.testmvp.ui.base.BaseActivity
import javax.inject.Inject

class CategoryActivity : BaseActivity(), CategoryContract.View {

    @Inject
    lateinit var presenter: CategoryContract.Presenter<CategoryContract.View>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_category)
        presenter.onAttach(this)
    }
}