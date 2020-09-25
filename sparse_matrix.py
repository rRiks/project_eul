def show(mat):
    for row in mat:
        for element in row:
            print(element,end = " ")
        print()
def sparse(mat):
    sparse_mat = []
    for row in range(len(mat)):
        for element in range(len(mat[row])):
            if mat[row][element] != 0:
                a=[]
                a.append(row)
                a.append(element)
                a.append(mat[row][element])
                sparse_mat.append(a)
    show(sparse_mat)
if __name__ == "__main__":
    matrix = [[int(input()) for i in range(3)]for j in range(3)]
    show(matrix)
    sparse(matrix)