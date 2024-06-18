x=int(input("enter the number"))
x1=0
x2=1
for z in range(0,x):
    if z<=1:
       x3=z
    else:
        x3=x1+x2
        x1=x2
        x2=x3
    print(x3,end=" ")