

x = input()
if len(x) == 0:
    print("invalid entry")
y = []
for i in range(len(x)-1):
    z= x[i] +x[i+1]
    y.append(z)
p = {}
for i in y:
    p[i] = y.count(i)
print(p)