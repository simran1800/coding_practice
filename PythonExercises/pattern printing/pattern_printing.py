#pattern printing using * 

n=int(input("enter a number for drawing your pattern\n"))
b=int(input("enter (1/0)\n"))
bb=bool(b)

if bb==True:
    for i in range(1,n+1):
        print("*"*i)

if bb==False:
    for i in range(n,0,-1):
        print("*"*i)