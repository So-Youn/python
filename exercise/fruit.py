# 장바구니에 아래와 같은 과일이 들어 있고 과일 판별 리스트가 있습니다. 현재 장바구니에는 과일이 몇 개이고,
# 과일이 아닌 것은 몇 개인지 출력하시오.

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}

fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

fruit_count = 0
not_fruit_count = 0

for key,val in basket_items.items(): # key, value 모두 가져올 수 있도록
    # print(key, val)
    if key in fruits : # key값이 fruits 안에 들어있는 지 확인
        fruit_count += val
    else :
        not_fruit_count += val
print(f'과일의 갯수는 {fruit_count}개, 과일이 아닌 것은 {not_fruit_count}개 있습니다.')
