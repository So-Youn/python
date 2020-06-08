# 함수 만들어 보자.
def hello():
    print("Hello, World!")
# print(hello()) # None


def hello():
    greeting = "Hello World!"
    return greeting
print(hello())

def sum(num1,num2) :
    return num1 + num2
my_num = 3
my_num2 = 4
k = sum(my_num,my_num2)
print(k)


    