import requests
import random

response = requests.get('https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=913')
# print(response)  #  <Response [200]> : 성공
# print(response.json)
# print(type(response.json()))

winner = []
data = response.json()
# print(dir(winner))
# winner.append(data['drwtNo1'])
for i in range(1,7) :
    winner.append(data[f'drwtNo{i}'])
    #winner.append(data['drwtNo'+str(i)])
print(winner) 

win_rate = {
    '1st' : 0,
    '2nd' : 0,
    '3rd' : 0,
    '4th' : 0,
    'fail' : 0,
}
for i in range(1000):
    lotto = random.sample(range(1,46),6)

    matched = 0 
    for num in lotto:
        if num in winner :
            matched += 1

    # 1. matched == 6 :  1등
    if matched == 6 :
        #print("1등")
        win_rate['1st'] += 1
    # 2. 5면 3등
    elif matched == 5 :
        #print("3등")
        if data['bnusNo'] in lotto:
            win_rate['2nd'] += 1
        else :
            win_rate['3rd'] += 1
    # 3. 4면 4등
    elif matched == 4 :
        win_rate['4th'] += 1
        #print("4등")
    # 4. 그 외는 fail
    else : 
        #print("fail")
        win_rate['fail'] +=1

print(win_rate)
