from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    menu = ['닭갈비','탕수육','초밥','스파게티돈까스']
    pick = random.choice(menu)
    return render(request, 'hello.html',{'pick':pick})
def name(request):
    my_name = '윤소윤'
    return render(request, 'name.html', {'my_name':my_name})
def introduce(request):
    my_info = ['윤소윤','26']   # 리스트 변수에 넣기
    name = '윤소윤'
    age = '26'
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'myinfo.html',context)
def forme(request):
    name = '윤소윤'
    dep = '전자공학부'
    birth = '95/01/02'
    git = 'https://github.com/So-Youn'
    about_me = {
        'name' : name,
        'dep' : dep,
        'birth' : birth,
        'git' : git
    }
    return render(request, 'forme.html', about_me)

# url로 매개변수 입력받기
def yourname(request,name):
    #name = name
    context = {
        'name' : name
    }
    return render(request,'yourname.html',context)
    
def nameage(request,name,age):
    context = {
        'name' : name,
        'age' : age
    }
    return render(request,'nameage.html',context)
def multiple(request,num1,num2):
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : num1 * num2
    }
    
    return render(request, 'multiple.html', context)

# 구구단 리스트 만들기
# 첫번째 숫자만큼 반복하는데 range(1,num1)
# for data in range(1,num1)
# num 2
# list.append(data*num2)
def gugu(request,big,small):
    result = []
    if big < small :
      big,small = small,big
    for num in range(1,small+1):
      result.append(big*num)
    context = {
      'result' : result
    }
    return render(request, 'gugu.html',context)

def dtl(request):
    my_list = ['짜장면','차돌짬뽕','탕수육','콩국수']
    empty_list = []
    my_string = "Life is short, you need Python"
    today = datetime.now()
    context = {
      'my_list' : my_list,
      'empty_list' : empty_list,
      'my_string' : my_string,
      'today' : today
    }
    return render(request, 'dtl.html',context)
    
def forif(request):
    my_list = [100,50,30,20,10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a,data_b = data_b,data_a
    context = {
      'my_list':my_list,
      'my_string' : my_string,
      'data_a' : data_a,
      'data_b' : data_b,
      
    }
    return render(request, 'forif.html',context)

