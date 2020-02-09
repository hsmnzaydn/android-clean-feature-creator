package com.basefy.testmvp.ui.command

import android.os.Bundle
import com.basefy.testmvp.R
import com.basefy.testmvp.ui.base.BaseActivity
import javax.inject.Inject

class CommandActivity : BaseActivity(), CommandContract.View {
    @Inject
    lateinit var presenter: CommandContract.Presenter<CommandContract.View>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_command)
        presenter.onAttach(this)

        presenter.write()
    }
}