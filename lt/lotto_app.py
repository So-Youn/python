# 모듈화
from lt import lottos

pick = lottos.lotto()
print(pick)

# 1. 만약 4등한 적이 있으면 4th >= 1,
# 2. 4등 `몇번` 했습니다.

# print(list(pick.keys('4th')))
# # lotto('str')
# fourth = list(pick.keys('4th'))
# def howmany() :
#     return fourth in pick().
# print()

count = pick['4th']
if count>=1 :
    print(f'4등은 {count}번 했습니다')


if pick['4th']>=1 :
    print(f'4등 {pick["4th"]}번 했습니다.')
else :
    print("fail")