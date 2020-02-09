package com.basefy.testmvp.ui.komut

import android.os.Bundle
import com.basefy.testmvp.R
import com.basefy.testmvp.ui.base.BaseActivity
import javax.inject.Inject

class KomutActivity : BaseActivity(), KomutContract.View {
    @Inject
    lateinit var presenter: KomutContract.Presenter<KomutContract.View>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.xmlName)
        presenter.onAttach(this)
    }
}