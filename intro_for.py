# 반복문 종류 2개
# 1. while

# while n < 3 :
#    print(n)
#    n +=1  # 0 1 2 

n=0
while n < 3 :
    n +=1
    print(n) 
print(n)   # 1 2 3 3

# 2. for
# number = list(range(10))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(number)
# number1 = list(range(3,10))   # [3, 4, 5, 6, 7, 8, 9]
# print(number1)
# number2 = list(range(3,10,3))  # [3, 6, 9]
# print(number2)


# 0 1 2 3 4 5 6 7 8 9
for num in range(10):
    print(num)

# 2 - 1 . list for
number = [10,9,8,7,6,5,4,3,2,1,0]
for num in number :
    print(num)

number = ['삼성', '역삼','선릉', '영등포']
for num in number :
    print(num)

# 2 - 2. idx로 접근
for i in range(len(number)):
    print(i)
    print(number[i])
# 2 - 3 enumerate
for idx, i in enumerate(number):
    print(idx, i)

# 3. dictionary
mask = {
    '삼성' : 100,
    '역삼' : '50개',
    '선릉' : True
}
for i in mask :
    print(i)
# 삼성
# 역삼
# 선릉

print("*"*30)
for i in mask.keys() : # 동작은 위와 동일하지만, dict라는 것을 표현하기 위함
    print(i)
    print(mask[i])

print("*"*30)
for i in mask.values():
    print(i)

print("*"*30)
for key, val in mask.items():
     print(key)
     print(val)
     print(mask[key])

for idx, i in enumerate(mask,3) :
    print(idx, i)
