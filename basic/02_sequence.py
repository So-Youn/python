# sequence - 데이터의 순차적 나열
# 주의할 점 : 정렬되어 있다는 뜻은 아님
# list, tuple, range, string
# 1. list
list_a = []
list_b = list()
list_a = ['삼성',23,True]
# 1-1.  idx로 접근하기
print(list_a[0])
print(list_a[-1]) # 맨 뒤 출력

# 2. tuple
tuple_a  = ()
tuple_a = (1,2)
print(tuple_a)
# tuple - 값을 하나만 넣고자 한다면 
tuple_b = (1,)      # <class 'tuple'>
tuple_c = (1)       # <class 'int'>
# print(type(tuple_b), type(tuple_c))
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
result = t1 + t2
print(result)
# # 3. range
print(range(10))
print(type(range(10))) 
print(list(range(10)))  # 0 ~ 9
print(list(range(3,10,2))) # 2씩 건너뛰면서 출력
