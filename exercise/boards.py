# 제시된 url을 통해 게시글 정보를 받아와 userId가 4인 유저가 작성한 모든 게시글의 제목을 출력하시오.
import requests
url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url).json()
mask_info={}
for data in response:
    if data['userId'] == 4:
       print(data['title'])