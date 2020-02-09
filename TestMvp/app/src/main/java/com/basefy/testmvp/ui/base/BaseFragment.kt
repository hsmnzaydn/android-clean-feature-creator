package com.basefy.testmvp.ui.base

import android.app.ProgressDialog
import android.content.Context
import android.os.Bundle
import com.basefy.testmvp.ui.base.BaseActivity
import com.basefy.testmvp.ui.base.MvpView
import dagger.android.support.DaggerFragment


abstract class BaseFragment : DaggerFragment(), MvpView {

    private var baseActivity: BaseActivity? = null
    private var progressDialog: ProgressDialog? = null


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setHasOptionsMenu(false)
    }

    override fun onAttach(context: Context) {
        super.onAttach(context)
        if (context is BaseActivity) {
            this.baseActivity = context
            context.onFragmentAttached()
        }
    }


    override fun showLoading() {
        baseActivity!!.showLoading()
    }


    override fun hideLoading() {

    }

    interface Callback {

        fun onFragmentAttached()

        fun onFragmentDetached(tag: String)
    }
}