def recursee(n):
    if n==1:
        return n
    else:
        return n*recursee(n-1)
num=int(input())
if num<0:
    print("no factorial for -ve numbers")
elif num==0:
    print("1")
else:
    print(recursee(num))
