package com.basefy.testmvp.Category.domain.usecases

import com.basefy.testmvp.Category.domain.repository.CategoryRepository
import javax.inject.Inject

class CategoryUseCase @Inject constructor(private val categoryRepository: CategoryRepository){

    fun writeCode(){
        categoryRepository.writeTest()
    }
}