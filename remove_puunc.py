


x= input("enter name:")
print(x[0].upper(),end=" ")
for i in range(1,len(x)-1):
    if x[i] == ' ':
        print(x[i+1].upper() , end=" ")