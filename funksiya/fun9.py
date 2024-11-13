def addLeftDigit(x, k):
    # 123, 5
    # 12 , 4
    # 1234566, 4
    x1=x
    honasoni=0
    while x>0:
        a=x%10
        x=x//10
        honasoni+=1
    # 5123
    # 412
    print(10**(honasoni)*k+x1)

addLeftDigit(27, 8)
addLeftDigit(144, 9)