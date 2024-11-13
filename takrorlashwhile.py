n=12
yigindi=0
kopaytma=1
while n>0:
    a=n%10
    yigindi+=a
    kopaytma*=a
    n=n//10
print(yigindi, kopaytma)