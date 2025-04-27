x = 121
tempX = x
reversedX = 0
if x < 0:
    print(False)
else:
    while tempX != 0:
        temp = tempX % 10
        reversedX = reversedX*10 + temp
        tempX = (tempX-temp)/10
    if reversedX == x:
        print(True)
    else: print(False)

print(str(x)==str(x)[::-1])
