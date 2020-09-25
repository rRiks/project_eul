pos = -1
def search(lst,n):
    L= 0
    U= len(lst) - 1
    while L<=U:
        mid = (L+U) //2
        M = lst[mid]
        if M == n:
            globals()['pos'] = mid
            return True
        else:
            if M<n:
                L = mid + 1
            else:
                U=mid - 1
    return False
list=[2,3,4,5,6,7,8,9,10]
n = int(input())
if search(list,n):
    print("found at index",pos)
else:
    print("not found")