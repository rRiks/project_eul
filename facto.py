

def fact(n):
    x=1
    if n==0:
        print(x)
    elif n<0:
        print("invalid input")
    else:
        for i in range(1,n+1):
           x=x*i

        print(x)

n=int(input())
fact(n)