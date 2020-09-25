max =0
z = []
y =[]
match =['1','2','3','4','5','6','7','8','9']
for i in range(9,9999):
    x = ''
    mul = 1
    while len(x)<9:
        x = x + str(i*mul)
        mul = mul + 1
    if len(x) == 9 and sorted(x) == match:
        z.append(x)
        y.append(i)
for i in range(len(z)):
    if int(z[i])>max:
        max = int(z[i])
print(max)
print(y)