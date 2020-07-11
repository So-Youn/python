# break
i = 0

while True:
    print("{}번째 반복문.".format(i))
    i = i + 1
    # 반복 종료
    input_text = input(">종료하시겠습니까?(y):")
    if input_text in ["y","Y"]:
        print("반복을 종료한다.")
        break

# continue
numbers = [5,15,6,20,7,25]
for number in numbers:
    # number가 10보다 작으면 다음 반복으로 넘어간다.
    if number < 10:
        continue
    print(number)



example_list = ["요소A","요소B","요소C"]
i = 0
for item in example_list:
    print("{}번째 요소는 {}입니다.".format(i,item))
    i += 1


### enumerate()
#단순 출력
print(example_list)
print()

# enumerate()함수에 적용
print("# enumerate()함수 적용")
print(enumerate(example_list))
print()

# list()함수로 강제 변환해 출력
print("# list()함수로 강제 변환 출력")
print(list(enumerate(example_list)))

#for문과 enumerate 함수 조합
print("# 반복문과 조합하기")
# enumerate()함수 사용시 반복 변수를 이런 형태로 넣을 수 있다.
for i , value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i,value))