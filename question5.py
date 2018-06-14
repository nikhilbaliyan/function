d=dict()
def factorial(num):
    if(num <=1):
        return 1
    else:
        a=num*factorial(num-1)
        d[0]=1
        d[1]=1
        d[num]=a
        return(num*factorial(num-1))
num= int(input("enter the number"))
print(factorial(num))
print(d)

