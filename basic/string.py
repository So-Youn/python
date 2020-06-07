result = "안녕안녕안녕안녕하세요".find("안녕")
print(result) # 처음 안녕이 0번째에

result_a = "안녕안녕안녕하세요".rfind("안녕")
print(result_a) # 4



a = "10 20 30 40 50".split(" ")
print(a)

# in 연산자
number = input("정수 입력>")
last_character = number[-1]

#짝수 조건
if last_character in "02468":
    print("짝수")
elif last_character in "13579":
    print("홀수")