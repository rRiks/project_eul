

for i in range(200,400):
    for j in range(i+1,400):
        if (i*i) + (j*j) == (1000-i-j)**2:
            print(i*j*(1000-i-j))