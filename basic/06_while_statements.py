import time
# while 
# 내가 준 조건이 참(True)인 동안
a = ''
while a !="안녕":
    print("안녕이라고 말할 때 까지 반복 할거야.")
    a = input("안녕이라고 말해 : ")


list_test=[1,2,1,2]
value=2

# 해당하는 값 모두 제거하기
while value in list_test:
    list_test.remove(value)

print(list_test)

# 유닉스 타임
number = 0
# 5초 동안 반복
# 즉, 5초동안 프로그램 정지시키기
target_tick = time.time()+5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복했다.".format(number))