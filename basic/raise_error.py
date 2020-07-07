number = input("정수 입력 >")
number = int(number)

if number > 0:
    print("양수")
    raise NotImplementedError
else:
    print("구현 안한 상태")
    raise NotImplementedError