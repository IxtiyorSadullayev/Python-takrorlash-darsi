# def salom():
#     name=input("Ismingizni kiriting: ")
#     print(f"Salom {name}")
#     print(f"Ismingiz belgilari soni {len(name)}")
# salom()
# salom()
# salom()
# salom()

def p(x):
    print(x)
# p("Hello")
# p(9)
# p("Ishladi")
def summ(a,b):
    p(a+b)
summ(4,5)

def fact(son): 
    k=1
    for x in range(1, son+1):
        k*=x 
    p(k)

fact(3)
fact(4)
fact(5)

# summ(1,2,3,4,5,566,7,7,8)
def summ2(*son):
    sonlar=list(son)
    yigindi=0
    for x in sonlar:
        yigindi+=x
    p(yigindi)

summ2(1,2,34,5,6,4)

def sonlar(*son:int):
    print(son)
sonlar(1,2,4,5,5.5)

def bio(name:str, fam:str, age:int):
    p(f"Sizning ismingiz {name}")
    p(f"Sizning familiyangiz {fam}")
    p(f"Sizning yoshingiz {age}")

bio("Rasul", "Baxtiyorov", 16)