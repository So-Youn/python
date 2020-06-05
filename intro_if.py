# 조건문
# 내장함수 = > built-in function

# input() - default가 string이다. >> int형은 형변환
# 형변환 string -> int

number = int(input())
#print(number + 3)

# 스트링으로 변환하려면? - str
# number = str(number)

# 1. if 조건문
# 들여쓰기를 기준으로 조건문 판단 ( = space bar 4번)
if number > 3:
    print("3초과")
print("???")

# 1 -2 조건을 여러개 쓰고 싶을 때
if number >10:
    print("10초과")
elif 10 >= number > 5 :
    print("애매")
else: 
    print("5이하")
# 조건문 순서대로 써주기
if number >10:
    print("10초과")
elif number > 5 :
    print("애매")
else: 
    print("5이하")



