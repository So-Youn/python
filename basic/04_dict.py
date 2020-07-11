dict_a = {
    "name" : "어벤져스 엔드게임",
    "type" : "히어로 무비"
}
print(dict_a["name"])
print(dict_a["type"])


dictionary = {}
print("요소 추가 이전:",dictionary)

dictionary["name"] = "윤소윤"
dictionary["age"] = "26"

print("요소 추가 이후:",dictionary)

name="이름"
dict_key = {
    name : "망고",
    type : "당절임"
}
print(dict_key)
value= dict_key.get("value")
print("값:",value)

if value == None:
    print("존재하지 않는 키에 접근했습니다.")