package com.hsmnzaydn.testmvvm.base

import android.app.ProgressDialog
import android.os.Bundle
import androidx.annotation.LayoutRes
import androidx.databinding.DataBindingUtil
import androidx.databinding.ViewDataBinding

import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.ViewModelProviders
import dagger.android.support.DaggerAppCompatActivity
import javax.inject.Inject


abstract class BaseActivity<T : ViewDataBinding, VM : BaseViewModel<BaseInterfaces>> :
    DaggerAppCompatActivity(),
    BaseInterfaces {

    var progressDialog: ProgressDialog? = null

    @LayoutRes
    abstract fun layoutRes(): Int

    abstract fun model(): Any

    protected lateinit var binding: T
        private set

    protected lateinit var viewModel: VM
        private set

    @Inject
    lateinit var viewModelFactory: ViewModelProvider.Factory


    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)

        binding = DataBindingUtil.setContentView(this, layoutRes())

        viewModel =
            ViewModelProviders.of(
                this,
                viewModelFactory
            ).get((model() as Class<VM>)).also {
                it.onAttach(this)
            }

    }





}