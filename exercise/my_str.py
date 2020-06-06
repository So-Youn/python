# 다음 문장의 모음을 제거하여 출력하세요.
my_str = "Life is too short, you need python"
for char in my_str:
    print(char)

#print(my_str[0]) # 문자열 index로 접근 가능

new_str = my_str.split(',') # space bar를 기준으로 단어 자르기
print(new_str)
# print(new_str[0][0])

print(my_str.find('a')) # 문자열이 없으면 -1이 뜸
print(my_str.index('a')) # 문자열이 없으면 아예 오류 발생


new_str = my_str.replace('Life','Time')
#print(new_str)

vowels = ['a','e','i','o','u']
for char in vowels:
    if char in my_str:
        my_str = my_str.replace(char,'')
        #print(list(my_str).sort()) - None 반환 - ? return 해주기

print(my_str)




