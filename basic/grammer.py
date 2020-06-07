# input
string = input("입력하세요>") # input의 리턴값이 string에 저장됨.
print(string)
print(type(string))

# format
# format함수로 숫자를 문자열로 변환하기
string_value = "{}".format(10)
print(string_value)
print(type(string_value))

format_a = "{}만원".format(5000)
format_b = "희망 연봉{}만원".format(5000)
format_c = "{}{}{}".format(3000,4000,5000)
format_d = "{}{}{}".format(1,"문자열",True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

