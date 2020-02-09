package com.basefy.testmvp.ui.home

import com.basefy.testmvp.R
import com.basefy.testmvp.ui.base.BaseActivity
import javax.inject.Inject

class HomeActivity : BaseActivity(), HomeContract.View {
    @Inject
    lateinit var presenter: HomeContract.Presenter<HomeContract.View>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.xmlName)
        presenter.onAttach(this)
    }
}