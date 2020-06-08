# 1. dictionary
# key, value로 이루어져 있음
dict_a = {}
dict_b = dict()
# key가 중복이 불가능하다.
dict_a = {'삼성':100,'역삼' : 50 , '삼성' : 30}  #덮어씌운다.
print(dict_a)

print(dict_a.keys())
print(dict_b.values())
print(dict_a.items()) # key, value 동시에

print(dict_a['삼성']) # value값 접근
print(dict_a.get('삼성'))  


# .get()과 []의 차이점
dict_a ={'삼성':100,'역삼' : 50}
print(dict_a.get('선릉')) # 오류 발생 x
# print(dict_a['선릉'])     # key 값이 없을 때 멈춰야 할 경우

# 2. set
# set는 순서가 없이 저장된다.
# 순서가 없다?  - index로 접근이 불가능하다
# sequence로 접근
# dictionary와 마찬가지로 중복이 없다.


set_a = {1,2,3}
set_b = {3,6,9}
# set_b = set()
print(set_a - set_b) # 차집합
print(set_a | set_b) # 합집합
print(set_a & set_b) # 교집합

list_a = [1,1,1,1]
print(list(set(list_a))[0]) # 중복 제거 

test = set("Hello")
print(test)
#Immutable 불가변성 mutable 가변
# list_a = [ ]
string = "immutable"
list_a = ['immutable?','real?']

print(string[0])
print(list_a[0])
string[0] = 'a'
list_a[0] = 'mutable' # 값을 바꿔준다
print(list_a)
list_a = ['mutable'] # 값을 할당




list_a = ['immutable?','real?']
list_b = list_a
print(list_a , list_b)
list_b[0] = 'mutable'
print(list_a,list_b)











