

def fib(n):
    x1 = 0
    x2 = 1
    while 1:
        x3=x1+x2
        if x3>=n:
            break
        else:
            x1 = x2
            x2 = x3
    print(x2)
n=int(input())
fib(n)

