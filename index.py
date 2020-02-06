import feature_creator.feature_creator as feature

print("Oluşturmak istediğiniz yapıyı seçiniz \n"
"1- Feature oluşturmak istiyorum\n"
"2- MVP View oluşturmak istiyorum\n"
"3- MVVM View oluşturmak istiyorum\n")

choose = input()



basePackage = "com.hsmnzaydn.term_commands_clean"

if choose == "1":
    print("Feature adı nedir?\n")
    featureName=input()
    feature.generateFeature(basePackage,featureName)

