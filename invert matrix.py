def show(mat):
    for row in mat:
        for element in row:
            print(element,end = " ")
        print()
def invert(mat):
    for i in range(len(mat)):
        for j in range(i,len(mat)):
            mat[i][j] , mat[j][i] = mat[j][i] , mat[i][j]
    for i in range(len(mat)):
        k = len(mat)-1
        for j in range(k):
            mat[j][i] ,mat[k][i]  = mat[k][i] , mat[j][i]
            k=k-1
    show(mat)
if __name__ == "__main__":
    x=input().split()
    matrix = [[int(i) for i in x in range(3)] for j in x in range(3)]
    #matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print("original matrix is:\n")
    show(matrix)
    print("inverted matrix is:\n")
    invert(matrix)