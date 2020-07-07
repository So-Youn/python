list_a = [127,32,103,"문자열",True,False]
list_a[3]
print(list_a[3])
list_a[3][0]
print(list_a[3][0])

# 리스트 안에 리스트 사용
list_b = [[1,2,3], [4,5,6], [7,8,9]]
list_b[1]
print(list_b[1])

print(list_b[1][1])

print(list_a*3)

list_c = [1,2,3]
print(list_c*3)

# 요소 제거
print("# 리스트 요소 하나 제거하기")
del1 = [0,1,2,3,4,5]
del del1[1]
print("del del1[1]>>", del1)

del1.pop(2)
print("del1.pop(2)>>", del1)