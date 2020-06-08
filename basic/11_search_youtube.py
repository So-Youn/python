from pprint import pprint
import requests


 # 데이터 key 값으로 접근하기
key = 'AIzaSyDTpklrqRhGlWUzUcWq0l9W54AIg__BZBk'
 # string interpolation
search = input("검색어를 입력해 주세요 ::::")
q = f'q={search}'
my_type = 'type=video'
part = 'part=snippet'
maxResults = 'maxResults=20'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}&{maxResults}'
print(url)

 # 1. 검색어를 입력하면
 # 2. 영상들을 검색
 # 3. 영상들의 제목과 채널명
response = requests.get(url)
data = response.json()


# 채널명, 영상 제목
# list 는 sequence이기 때문에 반복문으로 사용이 가능하다.

for data in data['items'][:10] :
    print(data['snippet']['title'],end ='채널명')   # snippet이 가지고 있는 data를 불러온다.
    print(data['snippet']['channelTitle'])





