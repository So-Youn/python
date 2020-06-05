# print("쓰고싶은 내용")

import random 
#print(dir(random)) # random이 가지고 있는 기능 

# choice를 써보자
number = random.choice(range(10)) # 0~ 9까지 중에 random 숫자 한개 추출
print(number)

# list에서 무작위로 뽑아보자
# arr = [100,50,30,20]
# pick = random.choice(arr)
# print(pick)

arr = ['100','50','30','20']
pick = random.choice(arr)
print(pick)

#dict에서도 써보자.
mask = {
    '100' : '삼성',
    '50' : '역삼',
    '30' : '선릉',
    '20' : '영등포'
}
print(mask[pick])

#sample 
lotto = random.sample(range(1,46), 6)
print(sorted(lotto)) # 정렬

