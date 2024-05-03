#работа со списками
my_list = ["чевапчичи", "пельмени", "сметана", "молоко", "сыр", "колбаса"]
print("список покупок: ",  my_list)
res = my_list[::len(my_list)-1]
print("Первый и последний элементы списка: ", res)
print("C третьего до пятого элементов: ", my_list[2:5])
my_list[2] = "помидоры"
print("Измененный список: ", my_list)
#работа со словарём
my_dict = {"Maxim": 88005553535, "Nicola": 89995559929, "Maman": 89775667333, "Koresh": 89654500720}
print(my_dict)
print("User number: ", my_dict["Nicola"])
my_dict.update({"Alex": 89735543433,
                "Alesha": 89443332727})
del my_dict["Koresh"]
print("Изменённый список: ", my_dict)