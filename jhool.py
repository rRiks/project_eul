T = int(input())
for i in range(T):
    N = int(input())
    A=[int(i) for i in input().split()]
    A.sort(reverse = True)
    cost = A[0]
    j = 1
    A.pop(0)
    while len(A) >0:
        cost = cost + j*A[0] +A[0]
        A.pop(0)
        j +=1

    print(cost)