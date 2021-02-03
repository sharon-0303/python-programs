number=int(input("Enter the total number of elements"))
print("Enter the elements")
mylist=[]
for i in range(0,number):
    n=input("Number ")
    mylist.append(n)
for j in range(0,number):
    for k in range(j+1,number):
        if(mylist[j]>mylist[k]):
            temp=mylist[j]
            mylist[j]=mylist[k]
            mylist[k]=temp
print(mylist)            
            
