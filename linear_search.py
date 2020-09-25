pos = 0


def search(lst,n):
    for i in range(len(lst)):
        if lst[i] == n:
            globals()['pos'] += i
            return True
    else:
        return False

list =[30,12,32,11,1,4,64,234,21,90]

n=90
if search(list,n) == True:
    print("found at index",pos)
else:
    print("not found")