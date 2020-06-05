# 2-2 . 가게 이름, 전화번호 출력
import random 
# 1 . 로또 번호 추첨하는데 5번 한번에 반복해서 출력
for i in range(5):
    print(sorted(random.sample(range(1,46),6)))
print("*"*30)
# 반복문을 한 줄로 쓸 때 - 컴프리핸션
lotto = [sorted(random.sample(range(1,46),6)) for i in range(5)]
print(lotto) 

#i = 0
# while i < 5 :
#     num = random.sample(range(1,46), 6)
#     print(num)
#     i +=1


# 2. 음식점 이름, 전화번호 dictionary -> 
food = {
    '엽떡' : '010-1234-5678',
    '반장떡볶이' : '010-1004-1008',
    '신전떡볶이' : '031-546-8575'
}
print(list(food.keys()))
# 2 - 1 . 그 중에서 무작위 음식점 하나 뽑아서
pick = random.choice(list(food.keys()))
print(pick)
print('가게이름은?', pick)
print('전화번호는?',food[pick])

# f- string 
print(f'가게이름은 {pick}, 전화번호는{food[pick]}')


# # for key,value in (mask,3) :
# #     print(key,value)
# random.choice(range(mask))
# 