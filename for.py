def bubblesort(e):
    swapped=False
    for n in range(len(e)-1,0,-1):
        for i in range(n):
            if e[i]>e[i+1]:
                swapped=True
                e[i],e[i+1]=e[i+1],e[i]
            if not swapped:
                return
t=[11,32,45,67,87,10,35,66]
bubblesort(t)
# print(e)

print("Sorted array : ")
print(t)