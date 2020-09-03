x = [1,2,4,6,8,2,34,6,9,345,8,245,78657,1,32,134,75]

def selection_sort(x):
    lowest = x[0]
    for start in range(len(x)-1):
        for i in range(len(x)-1-start):
            if x[i]<lowest:
                x[start]=x[i]
    return x
print(selection_sort(x))