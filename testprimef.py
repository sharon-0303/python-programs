num=int(input())
for i in range(2,num+1):
    if(num%i==0):
        print(num)
        for j in range(2,(i//2+1)):
            if(i%j==0):
                break
        
        

        
