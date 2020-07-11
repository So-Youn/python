a = range(5)
print(a)
# 매개변수 갯수 변경
b = list(range(10))
print(b)
c = list(range(0,10,3))
print(c)

b = range(0,10+1)
print(list(b))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 수식에 나누기 연산자 사용
n = 10
# a = range(0,n/2)
# print(a)  # TypeError 발생

## 나누기 연산자
a = range(0, n//2)
print(list(a))


#for 반복문과 범위
for i in range(5):
    print(str(i)+"= 반복 변수")
print("*"*10)

for i in range(0,10,3):
    print(str(i)+"=반복 변수")
print("*"*10)


print("리스트와 범위 조합해서 사용하기")
array = [273,32,103,57,52]
for i in range(len(array)):
    print("{}번째 반복:{}".format(i, array[i]))

# 역 반복문 - 1
for i in range(4,0 -1,-1): # 0까지 반복하고 싶어서 이 코드를 사용했다고 강조
    print("현재 반복 변수:{}".format(i))
# 역 반복문 - 2
for i in reversed(range(5)):
    print("현재 반복 변수:{}".format(i))