package com.hsmnzaydn.testmvvm.ui.category

import android.os.Bundle
import androidx.lifecycle.Observer
import com.hsmnzaydn.testmvvm.ui.category.CategoryViewModel
import com.hsmnzaydn.testmvvm.R
import com.hsmnzaydn.testmvvm.base.BaseActivity
import com.hsmnzaydn.testmvvm.base.BaseInterfaces
import com.hsmnzaydn.testmvvm.databinding.ActivityCategoryBinding

class CategoryActivity :
    BaseActivity<ActivityCategoryBinding, CategoryViewModel<BaseInterfaces>>() {

    override fun layoutRes(): Int = R.layout.activity_category
    override fun model() = CategoryViewModel::class.java

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

    }
}