

def summ(n):
    sumi = 0
    sumi = sumi + n*(n+1)/2
    return sumi
t = int(input())
while (t != 0):
    N = int(input())
    Arr = [int(i) for i in input().split()]
    X = Arr[1] / Arr[0]
    A =[0] * N
    A1 = [0] *N
    A1[0] = Arr[0]
    for i in range(1,N-1):
        A1[i] = Arr[i] * Arr[i-1]
    A[0] = Arr[1] / X
    for j in range(1,N-1):
        A[j] = Arr[j+1] / A1[j]
    som = 0
    som2 = 0
    for k in A:
        som = som + summ(k)
    som2 = som2 + summ(som)
    t = t-1
    print(som2)