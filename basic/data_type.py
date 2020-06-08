# import sys
# max_num = sys.maxsize
# print(max_num)
# super_max = max_num * max_num
# print(super_max)
# print(type(super_max))

# # 1. 정수형
# number = 10
# float_num = 1.3
# complex_num = (3 + 3j)
# print(type(number),type(float_num),type(complex_num))

# 2. bool
print(type(True))
print(type(False))

print(False == 0)   # - True . 즉, 0 은 False처럼 사용 가능

# 3. 문자열
greeing = 'hi'
name = "kim"
print(greeing, name)

# 문자열 입력받기
# input()
age = input("나이를 입력해 주세요 : ")
print("나이 :", age)
print(type(age))
print(int(age)) # 형변환

# string interpolation
name = 'kim'
print("안녕하세요", name)
print('{},{}'.format(greeing,name)) # ~3.5 버전 이하에서 많이 사용
print(f'{greeing},{name}') # 3.6버전 이후부터 지원


# 연산과 출력 형태 지정
pi = 3.141592
print(f'원주율은{pi:.3}, 반지름 = 2 원의 넓이는{pi*2*2}')  # {pi:4} : 4글자만 
