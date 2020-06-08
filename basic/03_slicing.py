sample_list = list(range(31))
print(sample_list)    # 0 ~ 30
print(sample_list[3])
print(sample_list[3:24])  # 3~ 23
print(sample_list[5:-1]) 
print(sample_list[5:])   # 5 ~ 끝까지
print(sample_list[3:len(sample_list):2]) # 3부터 list길이까지 출력

# 생략하기
print(sample_list[3::2])
print(sample_list[::2])
print(sample_list[::-1]) # 처음부터 반대로 출력


