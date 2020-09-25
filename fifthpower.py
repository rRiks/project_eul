x = []
y = 0

for j in range(2,1000000):
    z = str(j)
    m =0
    for k in z:
        m = m+ int(k)**5
    if m == j:
        y = y+j
print(y)
