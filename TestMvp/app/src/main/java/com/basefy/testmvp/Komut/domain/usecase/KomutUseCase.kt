package com.basefy.testmvp.Komut.domain.usecases

import com.basefy.base_mvvm_libraries.network.BaseServiceCallback
import com.basefy.testmvp.Komut.domain.repository.KomutRepository
import com.basefy.testmvp.base.BaseResponseCallback
import javax.inject.Inject

class KomutUseCase @Inject constructor(private val komutRepository: KomutRepository){

}