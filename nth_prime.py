
def isPrime(p):
    x = True
    for i in range(2,int(p**.5)+1):
        if p%i == 0:
            x= False
    return x
count = 0
ist = 3
while count < 10000:
    if isPrime(ist):
        count += 1
    ist +=2
print(ist-2)