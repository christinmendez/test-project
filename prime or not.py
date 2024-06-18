num=int(input("enter a positive number :  "))
if num == 1:
    print(num,"it is not a prime number")
elif num >1:
    for i in range(2,num):
        if(num%i)==0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")
