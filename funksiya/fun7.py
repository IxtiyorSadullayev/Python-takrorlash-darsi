def inverDIGIT(x):
    # 123
    if x<0:
        x=x*-1
    while x>0:
        a=x%10
        print(a,end="")
        x=x//10

inverDIGIT(1234)