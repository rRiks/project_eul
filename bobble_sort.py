

def sort(lst):
    for i in range(len(lst) - 1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] =temp
    return lst
lst1 = [4,2,7,5,1,3,6]
lst = sort(lst1)
print(lst)