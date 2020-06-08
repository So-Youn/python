# 1. 논리연산자
# and , or , not
print("___and___")
print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("___or___")
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print("___not___")
print(not True)
print(not False)
print(not [])   # {}, [] 모두 False

# in , not in
print("___in___")
print('a' in 'apple')
print(1 not in [1,2,3])


print("단순 평가")
print('' or 'Text' or 'Text2')  
# or는 하나만 계산되면 뒤를 넘어가기 때문에 Text 출력
print('Text' and '' or 'Text_2') # False or Text_2
