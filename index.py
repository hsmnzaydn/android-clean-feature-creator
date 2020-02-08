import feature_creator.feature_creator as feature
import mvp_creator.mvp_creator as mvp

print("Oluşturmak istediğiniz yapıyı seçiniz \n"
"1- Feature oluşturmak istiyorum\n"
"2- Presenter oluşturmak istiyorum\n"
"3- ViewModel oluşturmak istiyorum\n")

choose = input()



basePackage = "com.basefy.burger_king"

if choose == "1":
    print("Feature adı nedir?\n")
    featureName=input()
    feature.generateFeature(basePackage,featureName)

if choose == "2":
    print("Oluşturmak istediğiniz Presenter Adı\n")
    presenterName = input()
    print("Fragment için \"Fragment\" yazınız\n"
          "Activity için \"Activity\" yazınız\n")
    viewType= input()
    mvp.generatePresenter(presenterName,basePackage,viewType)
    
if choose == "3":
    print("Oluşturmak istediğiniz ViewModel Adı")
    viewModelName = input()

