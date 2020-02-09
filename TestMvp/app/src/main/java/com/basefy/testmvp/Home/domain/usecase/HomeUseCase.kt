package com.basefy.testmvp.Home.domain.usecases

import com.basefy.testmvp.Home.domain.repository.HomeRepository
import javax.inject.Inject

class HomeUseCase @Inject constructor(private val homeRepository: HomeRepository){

}