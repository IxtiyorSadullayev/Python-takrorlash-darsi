def sortinc3(a,b,c):
    if a<b<c:
        print(a,b,c)
    elif a<c<b:
        print(a,c,b)
    elif b<a<c:
        print(b,a,c)
    elif b<c<a:
        print(b,c,a)
    elif c<a<b:
        print(c,a,b)
    else:
        print(c,b,a)
        
# 5,9,8
# 5,8,9
sortinc3(7,10,2)
sortinc3(8,3,2)
sortinc3(5,6,7)
sortinc3(5,8,9)
sortinc3(9,1,6)

def kopson(*son):
    sonlar=list(son)
    sonlar.sort(reverse=True)
    print(sonlar)
kopson(3,2,5,6,20,99,1,72, 71, 7,4)