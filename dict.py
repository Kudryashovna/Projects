dict= {
"city":"Москва", 
"temperature":"20"
}
print(dict['city'])
dict["temperature"] = str(int(dict['temperature'])-5)
print(len(dict))
print(dict)
print(dict.get("country",0))
dict['country'] = "Россия"
print(dict)
dict['date'] = '27.05.2019'
print(len(dict))