# 특정 범위 혹은 , 시퀀스 같은
# 반복 가능한 객체의 요소들을 순차적으로

# 리스트와 for문 사용
for num in [1,2,3,4,5] :
    print(num)
print("끝")

print("리스트 선언")
array = [273,32,103,57,52]
for element in array:
    print(element)


print("반복문과 문자열")
for character in "안녕하세요":
    print("-", character)

for num in range(20):
    print(num)

# 조건과 같이
for num in range(1,31):
    # 연산자 중에 나머지만 구해주는 %
    # 0 == False
    # 1 == True
    if num % 2 :
        print(num)


# for_dictionary
dict_a = {
    '삼성' : 100,
    '역삼' : 50,
    '선릉' : 30
}
for data in dict_a :
    print(data)

for key, val in dict_a.items():
    print(key, val)

# 추가
num1 , num2 = 2,4
print(num1,num2)

