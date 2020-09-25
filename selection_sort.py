

def sort(lst):
    for i in range(len(lst)-1):
        min = i
        for j in range(i,len(lst)):
            if lst[j] < lst[min]:
                min = j

        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp

    return lst

lst =[ 8,1,2,5,29,6,4,7,10]
sort(lst)
print(lst)