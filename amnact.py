
def comDiv(n):
    sum = 0
    for i in range(1,int(n/2)+1):
        if n%i == 0:
            sum = sum+i
    return sum
def som(a):
    s = 0
    for i in range(len(a)):
        s = s+a[i]
    return s
if __name__ == "__main__":
    d = []
    R = []
    tot = 0
    for i in range(0,10001):
        d.append(comDiv(i))
    for j in range(1,10001):
        x = d[j]
        if x<10000:
            if d[x] == j and j!=x:
                R.append(j)

    print(som(R))
