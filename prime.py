print("enter the number")
num=int(input())
count=0
for i in range(2,num-1):
    if(num%i==0):
        count=count+1
if(count>0):
    print("not a prime number")
else:
    print("prime number")
    
