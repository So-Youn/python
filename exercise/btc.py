# 최고가와 최저가의 차이를 변동폭으로 정의할 때 
# (시가 + 변동폭)이 최고가 보다 높을 경우 '상승장',
# 그렇지 않을 경우 '하락장' 문자열을 출력하시오
# 시가 : 시작 거래 금액

import requests
url = 'https://api.bithumb.com/public/ticker/btc'
response = requests.get(url).json()['data'] # json 형태를 python에서 쓸 수 있도록 형태 변환
print(response)

fluctuation = int(response['max_price']) - int(response['min_price'])
# print(fluctuation) # 190000

if fluctuation + int(response['opening_price']) >= int(response['max_price']) :
    print("상승장")
else :
    print("하락장")
