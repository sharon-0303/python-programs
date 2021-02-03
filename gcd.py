def hcfn(m,n):
    if n==0:
        return m;
    else:
        return(n,m%n)

m1=int(input("Enter the first number"))
n1=int(input("Enter the second number"))
r=hcfn(m1,n1)
print(r)
