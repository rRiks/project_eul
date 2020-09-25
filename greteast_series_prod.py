x=''
y = []
ans = 1
final = 0
for i in range(20):
    g = input()
    x = x+g
for i in x:
    y.append(int(i))
print(y)
for i in range(988):
    for j in range(i,i+13):
        ans = ans* y[j]
    final = max(final,ans)
    ans  = 1
print(final)