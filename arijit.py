

t = int(input())
for _ in range(t):
    N = int(input())
    Arr =[]
    Arr = [int(i) for i in input().split()]
    A = [0] * N
    f =[0] * N
    som =0
    for j in range(1,N):
        A[j-1] = Arr[j] / Arr[j-1]
    for l in range(N-1):
        f[l] = A[l] * (A[l] +1) /2

        Q = sum(f)
        som = Q*(Q+1) / 2
    print(som)