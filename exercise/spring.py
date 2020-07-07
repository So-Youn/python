# 날짜/시간
import datetime

# 현재 날짜/시간
now = datetime.datetime.now()
month = now.month # 월 - 변수 지정
day = now.day #
# 계절 확인
if 3 <= month <= 5:
    print(f'현재는 {month}월{day}일, 봄')
elif 6 <= month <= 8:
    print(f'현재는 {month}월{day}일, 여름')
elif 9 <=month <= 11:
    print(f'현재는 {month}월{day}일, 가을')
else:
    print(f'현재는 {month}월{day}일, 겨울')