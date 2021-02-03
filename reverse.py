print("Enter the number")
rev=0
num=int(input())
while num>0:
    rev=rev*10+num%10
    num=num//10
print(rev)
