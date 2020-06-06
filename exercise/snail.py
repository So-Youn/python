def snail(height,day,night):
    count = 0
    while True :
        count += 1
        height -= day
        if height <=0 :
            return count
        height +=night
print(snail(100,5,2))