dict1 = {"city":"Moscow","temperature":"20"} #объявление словаря
dict1["temperature"]=int (dict1["temperature"])-5 #перевод элемнта в int, операция с ним
print(dict1)  #печать всех значений словаря
print(dict1.get("country")) #проверка наличия ключа country
dict1["country"]="russia" #добавление элемента в словарь
print(dict1["country"]) #печать одного элемнта