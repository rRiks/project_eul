
y=4
mat = []
def matrix():
    global y
    global mat
    for i in range(y):
        a=[]
        for j in range(y):
            a.append(i+1)
        mat.append(a)
    for i in range(y):
        for j in range(y):
            print(mat[i][j],end = " ")
        print()
matrix()