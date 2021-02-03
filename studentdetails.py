print("Enter the details of student y/n")
choice=input()
while(choice=="y"):
    print("mark1")
    a=int(input())
    b=int(input())
    c=int(input())
    avg=(a+b+c)/3
    print("average ",avg)
    perc=(avg/300)*100
    print(perc)
if 80 <= avg >=100:
    print("distinction")
        
    
    
    
