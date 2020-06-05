

# 함수는 원래 return 값이 있기 때문에 그냥 호출 시 None이 나온다.
# 따라서 return을 안에 꼭 넣어준다.

# def hello():
#     print("Hello, World!")   # 함수를 실행만 했을 뿐 아무것도 넘겨주지 않는다.
# print(hello())

def hello():
    return "Hello, World!"
print(hello())

def add(num, number):
    return num + number
nums = add(3,4)
print(nums)

range(1,10,3)

def ran(num,number=10):
    return num + number

nums = ran(3)
print(nums)

def m_num(a,b) :
    print(a)
    print(b)
    return a - b
a = 3
b = 4
minus = m_num(b,a)
print(minus)

