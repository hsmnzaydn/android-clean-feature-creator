package com.hsmnzaydn.testmvvm.ui.komut

import android.os.Bundle
import androidx.lifecycle.Observer
import com.hsmnzaydn.testmvvm.ui.komut.KomutViewModel
import com.hsmnzaydn.testmvvm.R
import com.hsmnzaydn.testmvvm.base.BaseActivity
import com.hsmnzaydn.testmvvm.base.BaseInterfaces
import com.hsmnzaydn.testmvvm.databinding.ActivityKomutBinding

class KomutActivity : BaseActivity<ActivityKomutBinding, KomutViewModel<BaseInterfaces>>() {

    override fun layoutRes(): Int = R.layout.activity_komut
    override fun model() = KomutViewModel::class.java

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }
}